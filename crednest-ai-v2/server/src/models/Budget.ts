import mongoose, { Document, Schema } from 'mongoose';

export interface IBudget extends Document {
    userId: mongoose.Types.ObjectId;
    category: string;
    amount: number;
    period: string;
    startDate?: Date;
    endDate?: Date;
    createdAt: Date;
}

const BudgetSchema = new Schema<IBudget>(
    {
        userId: {
            type: Schema.Types.ObjectId,
            ref: 'User',
            required: true,
            index: true
        },
        category: {
            type: String,
            required: true
        },
        amount: {
            type: Number,
            required: true,
            min: 0
        },
        period: {
            type: String,
            enum: ['daily', 'weekly', 'monthly', 'yearly'],
            default: 'monthly'
        },
        startDate: Date,
        endDate: Date
    },
    {
        timestamps: true
    }
);

BudgetSchema.index({ userId: 1, category: 1 });

export default mongoose.model<IBudget>('Budget', BudgetSchema);
