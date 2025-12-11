"""
CredNest AI - Tool Registry
Defines all functions available to Groq AI
"""

def get_tool_definitions():
    """
    Returns all tool definitions for Groq function calling
    These are ONLY finance-related tools
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "check_loan_eligibility",
                "description": "Check if user is eligible for a loan based on their financial profile. Use when user asks about loan eligibility, qualification, or whether they can get approved for a loan. Covers personal loans, home loans, car loans, business loans, and education loans.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "monthly_income": {
                            "type": "number",
                            "description": "User's monthly income in Indian Rupees (INR)"
                        },
                        "credit_score": {
                            "type": "number",
                            "description": "CIBIL credit score between 300-900. Higher is better. 750+ is excellent."
                        },
                        "employment_type": {
                            "type": "string",
                            "enum": ["salaried", "self_employed", "business"],
                            "description": "Type of employment: salaried (job), self_employed (freelancer/professional), business (owns company)"
                        },
                        "loan_amount": {
                            "type": "number",
                            "description": "Desired loan amount in Indian Rupees"
                        },
                        "loan_type": {
                            "type": "string",
                            "enum": ["personal", "home", "car", "business", "education"],
                            "description": "Type of loan needed"
                        },
                        "existing_loans": {
                            "type": "boolean",
                            "description": "Whether user has existing loans or EMIs"
                        }
                    },
                    "required": ["monthly_income", "loan_amount", "loan_type"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_emi",
                "description": "Calculate monthly EMI (Equated Monthly Installment) for a loan. Use when user wants to know monthly payment amount, total interest payable, or yearly breakdown. Works for all loan types - personal, home, car, business, education.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_amount": {
                            "type": "number",
                            "description": "Principal loan amount in Indian Rupees"
                        },
                        "interest_rate": {
                            "type": "number",
                            "description": "Annual interest rate as percentage (e.g., 10.5 for 10.5% per annum). Typical ranges: Personal loan 10-16%, Home loan 8-10%, Car loan 8-12%"
                        },
                        "tenure_months": {
                            "type": "number",
                            "description": "Loan tenure in months. Example: 60 months = 5 years, 240 months = 20 years"
                        }
                    },
                    "required": ["loan_amount", "interest_rate", "tenure_months"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_application_guidance",
                "description": "Provide step-by-step loan application process guidance including timeline, documents, and tips. Use when user asks how to apply for loan, application steps, process, or timeline.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_type": {
                            "type": "string",
                            "enum": ["personal", "home", "car", "business", "education"],
                            "description": "Type of loan"
                        },
                        "employment_type": {
                            "type": "string",
                            "enum": ["salaried", "self_employed", "business"],
                            "description": "Employment type for personalized guidance"
                        }
                    },
                    "required": ["loan_type"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_financial_tips",
                "description": "Provide expert financial literacy tips and actionable advice on various personal finance topics. Use when user asks for tips, advice, how to improve, or learn about financial topics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {
                            "type": "string",
                            "enum": ["credit_score", "saving", "debt_management", "investment", "budgeting", "loan_management"],
                            "description": "Financial topic: credit_score (improving CIBIL), saving (building wealth), debt_management (paying off loans), investment (mutual funds, stocks), budgeting (expense management), loan_management (smart borrowing)"
                        }
                    },
                    "required": ["topic"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_document_checklist",
                "description": "Get complete list of required documents for loan application with explanations. Use when user asks what documents are needed, required papers, or documentation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_type": {
                            "type": "string",
                            "enum": ["personal", "home", "car", "business", "education"],
                            "description": "Type of loan"
                        },
                        "employment_type": {
                            "type": "string",
                            "enum": ["salaried", "self_employed", "business"],
                            "description": "Employment type as document requirements differ"
                        }
                    },
                    "required": ["loan_type", "employment_type"]
                }
            }
        }
    ]
