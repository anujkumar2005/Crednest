import express from 'express';
import {
    getBanks,
    getBankById,
    calculateEMI,
    checkLoanEligibility
} from '../controllers/financialController';
import { protect } from '../middleware/auth';

const router = express.Router();

// All financial routes are protected
router.get('/banks', protect, getBanks);
router.get('/banks/:id', protect, getBankById);
router.post('/calculate-emi', protect, calculateEMI);
router.post('/check-eligibility', protect, checkLoanEligibility);

export default router;
