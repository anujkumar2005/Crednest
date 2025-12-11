import { Request, Response } from 'express';
import User from '../models/User';

export const register = async (req: Request, res: Response): Promise<void> => {
    try {
        const { email, password, name } = req.body;

        // Validation
        if (!email || !password || !name) {
            res.status(400).json({
                success: false,
                error: 'Please provide email, password, and name'
            });
            return;
        }

        if (password.length < 6) {
            res.status(400).json({
                success: false,
                error: 'Password must be at least 6 characters'
            });
            return;
        }

        // Check if user exists
        const existingUser = await User.findOne({ email: email.toLowerCase() });
        if (existingUser) {
            res.status(400).json({
                success: false,
                error: 'Email already registered'
            });
            return;
        }

        // Create user
        const user = await User.create({
            email: email.toLowerCase(),
            password,
            name
        });

        // Generate token
        const token = user.generateAuthToken();

        res.status(201).json({
            success: true,
            message: 'Registration successful',
            token,
            user: {
                id: user._id,
                email: user.email,
                name: user.name
            }
        });
    } catch (error: any) {
        console.error('Registration error:', error);
        res.status(500).json({
            success: false,
            error: 'Registration failed. Please try again.'
        });
    }
};

export const login = async (req: Request, res: Response): Promise<void> => {
    try {
        const { email, password } = req.body;

        // Validation
        if (!email || !password) {
            res.status(400).json({
                success: false,
                error: 'Please provide email and password'
            });
            return;
        }

        // Find user (include password for comparison)
        const user = await User.findOne({ email: email.toLowerCase() }).select('+password');

        if (!user) {
            res.status(401).json({
                success: false,
                error: 'Invalid credentials'
            });
            return;
        }

        // Check password
        const isPasswordMatch = await user.comparePassword(password);

        if (!isPasswordMatch) {
            res.status(401).json({
                success: false,
                error: 'Invalid credentials'
            });
            return;
        }

        // Update last login
        user.lastLogin = new Date();
        await user.save();

        // Generate token
        const token = user.generateAuthToken();

        res.status(200).json({
            success: true,
            message: 'Login successful',
            token,
            user: {
                id: user._id,
                email: user.email,
                name: user.name
            }
        });
    } catch (error: any) {
        console.error('Login error:', error);
        res.status(500).json({
            success: false,
            error: 'Login failed. Please try again.'
        });
    }
};

export const getProfile = async (req: any, res: Response): Promise<void> => {
    try {
        const user = await User.findById(req.user._id);

        if (!user) {
            res.status(404).json({
                success: false,
                error: 'User not found'
            });
            return;
        }

        res.status(200).json({
            success: true,
            user: {
                id: user._id,
                email: user.email,
                name: user.name,
                age: user.age,
                gender: user.gender,
                phone: user.phone,
                city: user.city,
                state: user.state,
                country: user.country,
                occupation: user.occupation,
                company: user.company,
                monthlyIncome: user.monthlyIncome,
                profileCompleted: user.profileCompleted,
                createdAt: user.createdAt,
                lastLogin: user.lastLogin
            }
        });
    } catch (error: any) {
        console.error('Get profile error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to load profile'
        });
    }
};

export const updateProfile = async (req: any, res: Response): Promise<void> => {
    try {
        const allowedFields = [
            'name', 'age', 'gender', 'dateOfBirth', 'phone',
            'address', 'city', 'state', 'pincode',
            'occupation', 'company', 'monthlyIncome', 'bio'
        ];

        const updates: any = {};
        Object.keys(req.body).forEach(key => {
            if (allowedFields.includes(key)) {
                updates[key] = req.body[key];
            }
        });

        const user = await User.findByIdAndUpdate(
            req.user._id,
            updates,
            { new: true, runValidators: true }
        );

        if (!user) {
            res.status(404).json({
                success: false,
                error: 'User not found'
            });
            return;
        }

        res.status(200).json({
            success: true,
            message: 'Profile updated successfully',
            user: {
                id: user._id,
                email: user.email,
                name: user.name,
                age: user.age,
                gender: user.gender,
                phone: user.phone,
                city: user.city,
                state: user.state,
                occupation: user.occupation,
                monthlyIncome: user.monthlyIncome
            }
        });
    } catch (error: any) {
        console.error('Update profile error:', error);
        res.status(500).json({
            success: false,
            error: 'Failed to update profile'
        });
    }
};
