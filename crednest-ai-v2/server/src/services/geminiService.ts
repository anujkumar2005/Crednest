import { GoogleGenerativeAI, GenerativeModel } from '@google/generative-ai';
import config from '../config/environment';

interface ToolFunction {
    name: string;
    description: string;
    parameters: any;
    handler: (...args: any[]) => Promise<any>;
}

class GeminiAIService {
    private genAI: GoogleGenerativeAI;
    private model: GenerativeModel;
    private tools: Map<string, ToolFunction>;

    constructor() {
        this.genAI = new GoogleGenerativeAI(config.geminiApiKey);
        this.model = this.genAI.getGenerativeModel({ model: 'gemini-pro' });
        this.tools = new Map();
        this.registerTools();
    }

    private registerTools(): void {
        // EMI Calculator Tool
        this.tools.set('calculate_emi', {
            name: 'calculate_emi',
            description: 'Calculate EMI (Equated Monthly Installment) for a loan',
            parameters: {
                type: 'object',
                properties: {
                    principal: { type: 'number', description: 'Loan amount in rupees' },
                    rate: { type: 'number', description: 'Annual interest rate in percentage' },
                    tenure: { type: 'number', description: 'Loan tenure in months' }
                },
                required: ['principal', 'rate', 'tenure']
            },
            handler: this.calculateEMI
        });

        // Loan Eligibility Tool
        this.tools.set('check_loan_eligibility', {
            name: 'check_loan_eligibility',
            description: 'Check if user is eligible for a loan based on income and credit score',
            parameters: {
                type: 'object',
                properties: {
                    monthlyIncome: { type: 'number', description: 'Monthly income in rupees' },
                    loanAmount: { type: 'number', description: 'Desired loan amount' },
                    cibilScore: { type: 'number', description: 'CIBIL credit score (300-900)' }
                },
                required: ['monthlyIncome', 'loanAmount']
            },
            handler: this.checkLoanEligibility
        });

        // Financial Tips Tool
        this.tools.set('get_financial_tips', {
            name: 'get_financial_tips',
            description: 'Get personalized financial tips based on category',
            parameters: {
                type: 'object',
                properties: {
                    category: {
                        type: 'string',
                        enum: ['saving', 'investing', 'budgeting', 'debt', 'credit_score'],
                        description: 'Category of financial advice needed'
                    }
                },
                required: ['category']
            },
            handler: this.getFinancialTips
        });
    }

    private calculateEMI(principal: number, rate: number, tenure: number): any {
        const monthlyRate = rate / (12 * 100);
        const emi = (principal * monthlyRate * Math.pow(1 + monthlyRate, tenure)) /
            (Math.pow(1 + monthlyRate, tenure) - 1);
        const totalAmount = emi * tenure;
        const totalInterest = totalAmount - principal;

        return {
            emi: Math.round(emi),
            totalAmount: Math.round(totalAmount),
            totalInterest: Math.round(totalInterest),
            principal,
            rate,
            tenure
        };
    }

    private checkLoanEligibility(
        monthlyIncome: number,
        loanAmount: number,
        cibilScore: number = 750
    ): any {
        const maxEligibleLoan = monthlyIncome * 60; // 60x monthly income
        const isEligible = loanAmount <= maxEligibleLoan && cibilScore >= 650;

        let recommendation = '';
        if (!isEligible) {
            if (cibilScore < 650) {
                recommendation = 'Your CIBIL score is below the minimum requirement. Work on improving it to 650+.';
            } else {
                recommendation = `Your maximum eligible loan amount is ₹${maxEligibleLoan.toLocaleString('en-IN')}. Consider reducing the loan amount.`;
            }
        } else {
            recommendation = 'You are eligible for this loan! You can proceed with the application.';
        }

        return {
            eligible: isEligible,
            monthlyIncome,
            requestedAmount: loanAmount,
            maxEligibleAmount: maxEligibleLoan,
            cibilScore,
            recommendation
        };
    }

    private getFinancialTips(category: string): any {
        const tips: Record<string, string[]> = {
            saving: [
                'Follow the 50-30-20 rule: 50% needs, 30% wants, 20% savings',
                'Automate your savings with recurring deposits',
                'Build an emergency fund covering 6 months of expenses',
                'Use high-interest savings accounts or fixed deposits'
            ],
            investing: [
                'Start investing early to benefit from compound interest',
                'Diversify your portfolio across different asset classes',
                'Consider SIP (Systematic Investment Plan) for mutual funds',
                'Review and rebalance your portfolio annually'
            ],
            budgeting: [
                'Track all your expenses for at least a month',
                'Use budgeting apps to monitor spending in real-time',
                'Set realistic budget limits for each category',
                'Review and adjust your budget monthly'
            ],
            debt: [
                'Pay off high-interest debt first (avalanche method)',
                'Consolidate multiple debts if possible',
                'Avoid taking new debt while paying off existing ones',
                'Negotiate with lenders for better interest rates'
            ],
            credit_score: [
                'Pay all bills and EMIs on time',
                'Keep credit utilization below 30%',
                'Maintain a healthy mix of secured and unsecured credit',
                'Check your credit report regularly for errors'
            ]
        };

        return {
            category,
            tips: tips[category] || tips.saving
        };
    }

    async chat(message: string, conversationHistory: any[] = []): Promise<string> {
        try {
            // Build conversation context
            const context = this.buildContext(conversationHistory);

            // System prompt for financial assistant
            const systemPrompt = `You are CredNest AI, an expert financial advisor specializing in Indian finance. 
You help users with budgeting, loans, investments, insurance, and savings.
You have access to tools for EMI calculation, loan eligibility checking, and financial tips.
Always provide accurate, helpful advice in a friendly and professional manner.
Use Indian currency (₹) and context when discussing finances.`;

            const fullPrompt = `${systemPrompt}\n\n${context}\n\nUser: ${message}\n\nAssistant:`;

            const result = await this.model.generateContent(fullPrompt);
            const response = result.response;
            return response.text();

        } catch (error: any) {
            console.error('Gemini AI Error:', error);
            throw new Error(`AI service error: ${error.message}`);
        }
    }

    async chatWithTools(
        message: string,
        conversationHistory: any[] = []
    ): Promise<{ response: string; toolUsed?: string }> {
        try {
            // Check if message requires tool usage
            const toolMatch = this.detectToolUsage(message);

            if (toolMatch) {
                const toolResult = await this.executeTool(toolMatch.tool, toolMatch.params);
                const response = await this.formatToolResponse(toolMatch.tool, toolResult, message);
                return { response, toolUsed: toolMatch.tool };
            }

            // Regular chat without tools
            const response = await this.chat(message, conversationHistory);
            return { response };

        } catch (error: any) {
            console.error('Chat with tools error:', error);
            throw error;
        }
    }

    private detectToolUsage(message: string): { tool: string; params: any } | null {
        const lowerMessage = message.toLowerCase();

        // EMI calculation detection
        if (lowerMessage.includes('emi') || lowerMessage.includes('calculate')) {
            const amountMatch = message.match(/₹?\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*(?:lakh|lac|l)?/i);
            const rateMatch = message.match(/(\d+(?:\.\d+)?)\s*%/);
            const tenureMatch = message.match(/(\d+)\s*(?:year|yr|month|mon)/i);

            if (amountMatch && rateMatch && tenureMatch) {
                let amount = parseFloat(amountMatch[1].replace(/,/g, ''));
                if (lowerMessage.includes('lakh') || lowerMessage.includes('lac')) {
                    amount *= 100000;
                }

                const rate = parseFloat(rateMatch[1]);
                let tenure = parseInt(tenureMatch[1]);
                if (lowerMessage.includes('year') || lowerMessage.includes('yr')) {
                    tenure *= 12;
                }

                return {
                    tool: 'calculate_emi',
                    params: { principal: amount, rate, tenure }
                };
            }
        }

        // Loan eligibility detection
        if (lowerMessage.includes('eligible') || lowerMessage.includes('eligibility')) {
            const incomeMatch = message.match(/income.*?₹?\s*(\d+(?:,\d+)*)/i);
            const loanMatch = message.match(/loan.*?₹?\s*(\d+(?:,\d+)*)/i);

            if (incomeMatch && loanMatch) {
                return {
                    tool: 'check_loan_eligibility',
                    params: {
                        monthlyIncome: parseFloat(incomeMatch[1].replace(/,/g, '')),
                        loanAmount: parseFloat(loanMatch[1].replace(/,/g, ''))
                    }
                };
            }
        }

        // Financial tips detection
        if (lowerMessage.includes('tips') || lowerMessage.includes('advice')) {
            const categories = ['saving', 'investing', 'budgeting', 'debt', 'credit_score'];
            for (const cat of categories) {
                if (lowerMessage.includes(cat.replace('_', ' '))) {
                    return {
                        tool: 'get_financial_tips',
                        params: { category: cat }
                    };
                }
            }
        }

        return null;
    }

    private async executeTool(toolName: string, params: any): Promise<any> {
        const tool = this.tools.get(toolName);
        if (!tool) {
            throw new Error(`Tool ${toolName} not found`);
        }

        return tool.handler(params.principal || params.monthlyIncome,
            params.rate || params.loanAmount,
            params.tenure || params.cibilScore,
            params.category);
    }

    private async formatToolResponse(
        toolName: string,
        toolResult: any,
        originalMessage: string
    ): Promise<string> {
        const context = `User asked: "${originalMessage}"\n\nTool used: ${toolName}\nTool result: ${JSON.stringify(toolResult, null, 2)}`;

        const prompt = `Based on the tool result, provide a helpful, conversational response to the user. 
Include the key numbers and explain them clearly. Use Indian currency format (₹).

${context}

Provide a natural, helpful response:`;

        const result = await this.model.generateContent(prompt);
        return result.response.text();
    }

    private buildContext(history: any[]): string {
        if (!history || history.length === 0) return '';

        return history
            .slice(-5) // Last 5 messages for context
            .map(msg => `User: ${msg.message}\nAssistant: ${msg.response}`)
            .join('\n\n');
    }
}

export default new GeminiAIService();
