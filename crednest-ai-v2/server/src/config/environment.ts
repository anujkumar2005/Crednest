import dotenv from 'dotenv';

dotenv.config();

interface Config {
    port: number;
    nodeEnv: string;
    mongoUri: string;
    jwtSecret: string;
    jwtExpire: string;
    geminiApiKey: string;
    corsOrigin: string;
}

const config: Config = {
    port: parseInt(process.env.PORT || '5000', 10),
    nodeEnv: process.env.NODE_ENV || 'development',
    mongoUri: process.env.MONGODB_URI || 'mongodb://localhost:27017/crednest_ai',
    jwtSecret: process.env.JWT_SECRET || 'fallback-secret-key',
    jwtExpire: process.env.JWT_EXPIRE || '7d',
    geminiApiKey: process.env.GEMINI_API_KEY || '',
    corsOrigin: process.env.CORS_ORIGIN || 'http://localhost:3000'
};

// Validate required environment variables
if (!config.geminiApiKey) {
    console.warn('⚠️  GEMINI_API_KEY not set in environment variables');
}

if (!config.jwtSecret || config.jwtSecret === 'fallback-secret-key') {
    console.warn('⚠️  JWT_SECRET not set - using fallback (not secure for production)');
}

export default config;
