import { Response } from 'express';
import { AuthRequest } from '../middleware/auth';
import Bank from '../models/Bank';

export const getBanks = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { loanType, limit = '20' } = req.query;

        let sortField = 'rating';
        if (loanType === 'home') sortField = 'homeLoanRate';
        else if (loanType === 'personal') sortField = 'personalLoanRate';
        else if (loanType === 'car') sortField = 'carLoanRate';
        else if (loanType === 'education') sortField = 'educationLoanRate';

        const banks = await Bank.find()
            .sort({ [sortField]: 1, rating: -1 })
            .limit(parseInt(limit as string));

        res.status(200).json({
            success: true,
            count: banks.length,
            banks
        });
    } catch (error: any) {
        console.error('Get banks error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to load banks'
        });
    }
};

export const getBankById = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { id } = req.params;

        const bank = await Bank.findById(id);

        if (!bank) {
            res.status(404).json({
                success: false,
                error: 'Bank not found'
            });
            return;
        }

        res.status(200).json({
            success: true,
            bank
        });
    } catch (error: any) {
        console.error('Get bank error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to load bank details'
        });
    }
};

export const calculateEMI = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { principal, rate, tenure } = req.body;

        if (!principal || !rate || !tenure) {
            res.status(400).json({
                success: false,
                error: 'Principal, rate, and tenure are required'
            });
            return;
        }

        const monthlyRate = rate / (12 * 100);
        const emi = (principal * monthlyRate * Math.pow(1 + monthlyRate, tenure)) /
            (Math.pow(1 + monthlyRate, tenure) - 1);
        const totalAmount = emi * tenure;
        const totalInterest = totalAmount - principal;

        res.status(200).json({
            success: true,
            calculation: {
                principal,
                rate,
                tenure,
                emi: Math.round(emi),
                totalAmount: Math.round(totalAmount),
                totalInterest: Math.round(totalInterest),
                monthlyPayment: Math.round(emi)
            }
        });
    } catch (error: any) {
        console.error('Calculate EMI error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to calculate EMI'
        });
    }
};

export const checkLoanEligibility = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { monthlyIncome, loanAmount, cibilScore = 750 } = req.body;

        if (!monthlyIncome || !loanAmount) {
            res.status(400).json({
                success: false,
                error: 'Monthly income and loan amount are required'
            });
            return;
        }

        const maxEligibleLoan = monthlyIncome * 60; // 60x monthly income
        const isEligible = loanAmount <= maxEligibleLoan && cibilScore >= 650;

        let recommendation = '';
        let status = 'approved';

        if (!isEligible) {
            status = 'rejected';
            if (cibilScore < 650) {
                recommendation = 'Your CIBIL score is below the minimum requirement. Work on improving it to 650+.';
            } else {
                recommendation = `Your maximum eligible loan amount is ₹${maxEligibleLoan.toLocaleString('en-IN')}. Consider reducing the loan amount.`;
            }
        } else {
            recommendation = 'You are eligible for this loan! You can proceed with the application.';
        }

        res.status(200).json({
            success: true,
            eligibility: {
                eligible: isEligible,
                status,
                monthlyIncome,
                requestedAmount: loanAmount,
                maxEligibleAmount: maxEligibleLoan,
                cibilScore,
                recommendation
            }
        });
    } catch (error: any) {
        console.error('Check eligibility error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to check loan eligibility'
        });
    }
};
