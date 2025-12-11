import mongoose, { Document, Schema } from 'mongoose';

export interface IChatMessage extends Document {
    userId: mongoose.Types.ObjectId;
    sessionId: string;
    message: string;
    response: string;
    toolUsed?: string;
    createdAt: Date;
}

const ChatMessageSchema = new Schema<IChatMessage>(
    {
        userId: {
            type: Schema.Types.ObjectId,
            ref: 'User',
            required: true,
            index: true
        },
        sessionId: {
            type: String,
            required: true,
            index: true
        },
        message: {
            type: String,
            required: true
        },
        response: {
            type: String,
            required: true
        },
        toolUsed: String
    },
    {
        timestamps: true
    }
);

// Compound index for efficient queries
ChatMessageSchema.index({ userId: 1, sessionId: 1, createdAt: -1 });

export default mongoose.model<IChatMessage>('ChatMessage', ChatMessageSchema);
