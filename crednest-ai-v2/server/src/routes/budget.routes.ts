import express from 'express';
import {
    createBudget,
    getBudgets,
    updateBudget,
    deleteBudget,
    addExpense,
    getExpenses,
    deleteExpense,
    getBudgetSummary
} from '../controllers/budgetController';
import { protect } from '../middleware/auth';

const router = express.Router();

// All budget routes are protected
router.post('/budgets', protect, createBudget);
router.get('/budgets', protect, getBudgets);
router.put('/budgets/:id', protect, updateBudget);
router.delete('/budgets/:id', protect, deleteBudget);
router.get('/budgets/summary', protect, getBudgetSummary);

router.post('/expenses', protect, addExpense);
router.get('/expenses', protect, getExpenses);
router.delete('/expenses/:id', protect, deleteExpense);

export default router;
