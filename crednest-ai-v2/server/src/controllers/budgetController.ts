import { Response } from 'express';
import { AuthRequest } from '../middleware/auth';
import Budget from '../models/Budget';
import Expense from '../models/Expense';

export const createBudget = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { category, amount, period, startDate, endDate } = req.body;
        const userId = req.user!._id;

        if (!category || !amount) {
            res.status(400).json({
                success: false,
                error: 'Category and amount are required'
            });
            return;
        }

        const budget = await Budget.create({
            userId,
            category,
            amount,
            period: period || 'monthly',
            startDate,
            endDate
        });

        res.status(201).json({
            success: true,
            message: 'Budget created successfully',
            budget
        });
    } catch (error: any) {
        console.error('Create budget error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to create budget'
        });
    }
};

export const getBudgets = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const userId = req.user!._id;
        const { period } = req.query;

        const query: any = { userId };
        if (period) {
            query.period = period;
        }

        const budgets = await Budget.find(query).sort({ createdAt: -1 });

        res.status(200).json({
            success: true,
            count: budgets.length,
            budgets
        });
    } catch (error: any) {
        console.error('Get budgets error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to load budgets'
        });
    }
};

export const updateBudget = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { id } = req.params;
        const userId = req.user!._id;
        const updates = req.body;

        const budget = await Budget.findOneAndUpdate(
            { _id: id, userId },
            updates,
            { new: true, runValidators: true }
        );

        if (!budget) {
            res.status(404).json({
                success: false,
                error: 'Budget not found'
            });
            return;
        }

        res.status(200).json({
            success: true,
            message: 'Budget updated successfully',
            budget
        });
    } catch (error: any) {
        console.error('Update budget error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to update budget'
        });
    }
};

export const deleteBudget = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { id } = req.params;
        const userId = req.user!._id;

        const budget = await Budget.findOneAndDelete({ _id: id, userId });

        if (!budget) {
            res.status(404).json({
                success: false,
                error: 'Budget not found'
            });
            return;
        }

        res.status(200).json({
            success: true,
            message: 'Budget deleted successfully'
        });
    } catch (error: any) {
        console.error('Delete budget error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to delete budget'
        });
    }
};

export const addExpense = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { category, amount, description, date, paymentMethod } = req.body;
        const userId = req.user!._id;

        if (!category || !amount) {
            res.status(400).json({
                success: false,
                error: 'Category and amount are required'
            });
            return;
        }

        const expense = await Expense.create({
            userId,
            category,
            amount,
            description,
            date: date || new Date(),
            paymentMethod
        });

        res.status(201).json({
            success: true,
            message: 'Expense added successfully',
            expense
        });
    } catch (error: any) {
        console.error('Add expense error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to add expense'
        });
    }
};

export const getExpenses = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const userId = req.user!._id;
        const { category, startDate, endDate, limit = '50' } = req.query;

        const query: any = { userId };

        if (category) {
            query.category = category;
        }

        if (startDate || endDate) {
            query.date = {};
            if (startDate) query.date.$gte = new Date(startDate as string);
            if (endDate) query.date.$lte = new Date(endDate as string);
        }

        const expenses = await Expense.find(query)
            .sort({ date: -1 })
            .limit(parseInt(limit as string));

        // Calculate total
        const total = expenses.reduce((sum, exp) => sum + exp.amount, 0);

        res.status(200).json({
            success: true,
            count: expenses.length,
            total,
            expenses
        });
    } catch (error: any) {
        console.error('Get expenses error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to load expenses'
        });
    }
};

export const deleteExpense = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { id } = req.params;
        const userId = req.user!._id;

        const expense = await Expense.findOneAndDelete({ _id: id, userId });

        if (!expense) {
            res.status(404).json({
                success: false,
                error: 'Expense not found'
            });
            return;
        }

        res.status(200).json({
            success: true,
            message: 'Expense deleted successfully'
        });
    } catch (error: any) {
        console.error('Delete expense error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to delete expense'
        });
    }
};

export const getBudgetSummary = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const userId = req.user!._id;
        const { period = 'monthly' } = req.query;

        // Get budgets
        const budgets = await Budget.find({ userId, period });

        // Get expenses for current period
        const now = new Date();
        const startOfMonth = new Date(now.getFullYear(), now.getMonth(), 1);
        const endOfMonth = new Date(now.getFullYear(), now.getMonth() + 1, 0);

        const expenses = await Expense.find({
            userId,
            date: { $gte: startOfMonth, $lte: endOfMonth }
        });

        // Calculate summary by category
        const summary = budgets.map(budget => {
            const categoryExpenses = expenses.filter(exp => exp.category === budget.category);
            const spent = categoryExpenses.reduce((sum, exp) => sum + exp.amount, 0);

            return {
                category: budget.category,
                budgeted: budget.amount,
                spent,
                remaining: budget.amount - spent,
                percentage: (spent / budget.amount) * 100
            };
        });

        const totalBudget = budgets.reduce((sum, b) => sum + b.amount, 0);
        const totalSpent = expenses.reduce((sum, e) => sum + e.amount, 0);

        res.status(200).json({
            success: true,
            period,
            summary,
            totals: {
                budgeted: totalBudget,
                spent: totalSpent,
                remaining: totalBudget - totalSpent,
                percentage: totalBudget > 0 ? (totalSpent / totalBudget) * 100 : 0
            }
        });
    } catch (error: any) {
        console.error('Get budget summary error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to load budget summary'
        });
    }
};
