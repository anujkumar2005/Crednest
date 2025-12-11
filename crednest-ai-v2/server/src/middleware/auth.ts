import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import User, { IUser } from '../models/User';
import config from '../config/environment';

export interface AuthRequest extends Request {
    user?: IUser;
}

export const protect = async (
    req: AuthRequest,
    res: Response,
    next: NextFunction
): Promise<void> => {
    try {
        let token: string | undefined;

        // Check for token in Authorization header
        if (
            req.headers.authorization &&
            req.headers.authorization.startsWith('Bearer')
        ) {
            token = req.headers.authorization.split(' ')[1];
        }

        if (!token) {
            res.status(401).json({
                success: false,
                error: 'Not authorized to access this route'
            });
            return;
        }

        try {
            // Verify token
            const decoded = jwt.verify(token, config.jwtSecret) as { id: string };

            // Get user from token
            const user = await User.findById(decoded.id);

            if (!user) {
                res.status(401).json({
                    success: false,
                    error: 'User not found'
                });
                return;
            }

            if (!user.isActive) {
                res.status(401).json({
                    success: false,
                    error: 'User account is deactivated'
                });
                return;
            }

            req.user = user;
            next();
        } catch (error) {
            res.status(401).json({
                success: false,
                error: 'Invalid or expired token'
            });
            return;
        }
    } catch (error) {
        res.status(500).json({
            success: false,
            error: 'Server error in authentication'
        });
    }
};
