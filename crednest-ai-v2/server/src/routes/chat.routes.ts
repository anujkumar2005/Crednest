import express from 'express';
import {
    sendMessage,
    getChatHistory,
    getAllSessions,
    deleteSession
} from '../controllers/chatController';
import { protect } from '../middleware/auth';

const router = express.Router();

// All chat routes are protected
router.post('/message', protect, sendMessage);
router.get('/sessions', protect, getAllSessions);
router.get('/history/:sessionId', protect, getChatHistory);
router.delete('/session/:sessionId', protect, deleteSession);

export default router;
