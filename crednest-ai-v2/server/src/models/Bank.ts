import mongoose, { Document, Schema } from 'mongoose';

export interface IBank extends Document {
    name: string;
    logoUrl?: string;
    homeLoanRate?: number;
    personalLoanRate?: number;
    carLoanRate?: number;
    educationLoanRate?: number;
    processingFee?: number;
    minCibilScore?: number;
    maxLoanAmount?: number;
    minLoanAmount?: number;
    maxTenureYears?: number;
    description?: string;
    website?: string;
    customerCare?: string;
    rating?: number;
    lastUpdated: Date;
}

const BankSchema = new Schema<IBank>(
    {
        name: {
            type: String,
            required: true,
            unique: true
        },
        logoUrl: String,
        homeLoanRate: Number,
        personalLoanRate: Number,
        carLoanRate: Number,
        educationLoanRate: Number,
        processingFee: Number,
        minCibilScore: Number,
        maxLoanAmount: Number,
        minLoanAmount: Number,
        maxTenureYears: Number,
        description: String,
        website: String,
        customerCare: String,
        rating: {
            type: Number,
            min: 0,
            max: 5
        },
        lastUpdated: {
            type: Date,
            default: Date.now
        }
    },
    {
        timestamps: true
    }
);

BankSchema.index({ name: 1 });
BankSchema.index({ rating: -1 });

export default mongoose.model<IBank>('Bank', BankSchema);
