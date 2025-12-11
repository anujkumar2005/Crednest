import mongoose, { Document, Schema } from 'mongoose';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import config from '../config/environment';

export interface IUser extends Document {
    email: string;
    password: string;
    name: string;
    age?: number;
    gender?: string;
    dateOfBirth?: Date;
    phone?: string;
    address?: string;
    city?: string;
    state?: string;
    country: string;
    pincode?: string;
    occupation?: string;
    company?: string;
    monthlyIncome?: number;
    profileImage?: string;
    bio?: string;
    profileCompleted: boolean;
    isActive: boolean;
    isVerified: boolean;
    lastLogin?: Date;
    createdAt: Date;
    updatedAt: Date;
    comparePassword(candidatePassword: string): Promise<boolean>;
    generateAuthToken(): string;
}

const UserSchema = new Schema<IUser>(
    {
        email: {
            type: String,
            required: [true, 'Email is required'],
            unique: true,
            lowercase: true,
            trim: true,
            match: [/^\S+@\S+\.\S+$/, 'Please provide a valid email']
        },
        password: {
            type: String,
            required: [true, 'Password is required'],
            minlength: [6, 'Password must be at least 6 characters'],
            select: false
        },
        name: {
            type: String,
            required: [true, 'Name is required'],
            trim: true
        },
        age: Number,
        gender: {
            type: String,
            enum: ['Male', 'Female', 'Other', 'Prefer not to say']
        },
        dateOfBirth: Date,
        phone: String,
        address: String,
        city: String,
        state: String,
        country: {
            type: String,
            default: 'India'
        },
        pincode: String,
        occupation: String,
        company: String,
        monthlyIncome: Number,
        profileImage: String,
        bio: String,
        profileCompleted: {
            type: Boolean,
            default: false
        },
        isActive: {
            type: Boolean,
            default: true
        },
        isVerified: {
            type: Boolean,
            default: false
        },
        lastLogin: Date
    },
    {
        timestamps: true
    }
);

// Hash password before saving
UserSchema.pre('save', async function (next) {
    if (!this.isModified('password')) {
        return next();
    }

    const salt = await bcrypt.genSalt(10);
    this.password = await bcrypt.hash(this.password, salt);
    next();
});

// Compare password method
UserSchema.methods.comparePassword = async function (
    candidatePassword: string
): Promise<boolean> {
    return await bcrypt.compare(candidatePassword, this.password);
};

// Generate JWT token
UserSchema.methods.generateAuthToken = function (): string {
    return jwt.sign(
        { id: this._id.toString(), email: this.email },
        config.jwtSecret,
        { expiresIn: config.jwtExpire } as any
    );
};

// Index for faster queries
UserSchema.index({ email: 1 });
UserSchema.index({ createdAt: -1 });

export default mongoose.model<IUser>('User', UserSchema);
