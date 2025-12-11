import { Response } from 'express';
import { AuthRequest } from '../middleware/auth';
import ChatMessage from '../models/ChatMessage';
import geminiService from '../services/geminiService';
import { v4 as uuidv4 } from 'uuid';

export const sendMessage = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { message, sessionId } = req.body;
        const userId = req.user!._id;

        if (!message) {
            res.status(400).json({
                success: false,
                error: 'Message is required'
            });
            return;
        }

        // Generate session ID if not provided
        const chatSessionId = sessionId || uuidv4();

        // Get conversation history for context
        const history = await ChatMessage.find({
            userId,
            sessionId: chatSessionId
        })
            .sort({ createdAt: -1 })
            .limit(5)
            .lean();

        // Get AI response with tools
        const { response, toolUsed } = await geminiService.chatWithTools(
            message,
            history.reverse()
        );

        // Save to database
        const chatMessage = await ChatMessage.create({
            userId,
            sessionId: chatSessionId,
            message,
            response,
            toolUsed
        });

        res.status(200).json({
            success: true,
            sessionId: chatSessionId,
            message: chatMessage.message,
            response: chatMessage.response,
            toolUsed: chatMessage.toolUsed,
            timestamp: chatMessage.createdAt
        });
    } catch (error: any) {
        console.error('Chat error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to process message'
        });
    }
};

export const getChatHistory = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { sessionId } = req.params;
        const userId = req.user!._id;

        const messages = await ChatMessage.find({
            userId,
            sessionId
        })
            .sort({ createdAt: 1 })
            .lean();

        res.status(200).json({
            success: true,
            sessionId,
            messages: messages.map(msg => ({
                id: msg._id,
                message: msg.message,
                response: msg.response,
                toolUsed: msg.toolUsed,
                timestamp: msg.createdAt
            }))
        });
    } catch (error: any) {
        console.error('Get chat history error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to load chat history'
        });
    }
};

export const getAllSessions = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const userId = req.user!._id;

        const sessions = await ChatMessage.aggregate([
            { $match: { userId } },
            {
                $group: {
                    _id: '$sessionId',
                    lastMessage: { $last: '$message' },
                    lastResponse: { $last: '$response' },
                    messageCount: { $sum: 1 },
                    lastActivity: { $max: '$createdAt' }
                }
            },
            { $sort: { lastActivity: -1 } }
        ]);

        res.status(200).json({
            success: true,
            sessions: sessions.map(session => ({
                sessionId: session._id,
                preview: session.lastMessage.substring(0, 100),
                messageCount: session.messageCount,
                lastActivity: session.lastActivity
            }))
        });
    } catch (error: any) {
        console.error('Get sessions error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to load sessions'
        });
    }
};

export const deleteSession = async (req: AuthRequest, res: Response): Promise<void> => {
    try {
        const { sessionId } = req.params;
        const userId = req.user!._id;

        await ChatMessage.deleteMany({
            userId,
            sessionId
        });

        res.status(200).json({
            success: true,
            message: 'Session deleted successfully'
        });
    } catch (error: any) {
        console.error('Delete session error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to delete session'
        });
    }
};
