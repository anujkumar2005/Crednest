import mongoose, { Document, Schema } from 'mongoose';

export interface IExpense extends Document {
    userId: mongoose.Types.ObjectId;
    category: string;
    amount: number;
    description?: string;
    date: Date;
    paymentMethod?: string;
    createdAt: Date;
}

const ExpenseSchema = new Schema<IExpense>(
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
        description: String,
        date: {
            type: Date,
            required: true,
            default: Date.now
        },
        paymentMethod: {
            type: String,
            enum: ['Cash', 'Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Other']
        }
    },
    {
        timestamps: true
    }
);

ExpenseSchema.index({ userId: 1, date: -1 });
ExpenseSchema.index({ userId: 1, category: 1 });

export default mongoose.model<IExpense>('Expense', ExpenseSchema);
