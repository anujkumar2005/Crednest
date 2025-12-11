import express, { Application, Request, Response } from 'express';
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import config from './config/environment';
import connectDatabase from './config/database';

// Import routes
import authRoutes from './routes/auth.routes';
import chatRoutes from './routes/chat.routes';
import budgetRoutes from './routes/budget.routes';
import financialRoutes from './routes/financial.routes';

const app: Application = express();

// ============================================================================
// MIDDLEWARE
// ============================================================================

// Security
app.use(helmet());

// CORS
app.use(cors({
    origin: config.corsOrigin,
    credentials: true
}));

// Body parser
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Logging
if (config.nodeEnv === 'development') {
    app.use(morgan('dev'));
}

// ============================================================================
// ROUTES
// ============================================================================

// Health check
app.get('/health', (req: Request, res: Response) => {
    res.status(200).json({
        success: true,
        message: 'CredNest AI Server is running',
        timestamp: new Date().toISOString()
    });
});

// API routes
app.use('/api/auth', authRoutes);
app.use('/api/chat', chatRoutes);
app.use('/api', budgetRoutes);
app.use('/api/financial', financialRoutes);

// 404 handler
app.use((req: Request, res: Response) => {
    res.status(404).json({
        success: false,
        error: 'Route not found'
    });
});

// Error handler
app.use((err: any, req: Request, res: Response, next: any) => {
    console.error('Error:', err);
    res.status(err.status || 500).json({
        success: false,
        error: err.message || 'Internal server error'
    });
});

// ============================================================================
// SERVER INITIALIZATION
// ============================================================================

const startServer = async () => {
    try {
        // Connect to database
        await connectDatabase();

        // Start server
        app.listen(config.port, () => {
            console.log('');
            console.log('╔════════════════════════════════════════════════════════════╗');
            console.log('║                                                            ║');
            console.log('║              🏦 CredNest AI Server v2.0                   ║');
            console.log('║                                                            ║');
            console.log('╚════════════════════════════════════════════════════════════╝');
            console.log('');
            console.log(`✓ Server running on port ${config.port}`);
            console.log(`✓ Environment: ${config.nodeEnv}`);
            console.log(`✓ CORS enabled for: ${config.corsOrigin}`);
            console.log(`✓ Gemini AI: ${config.geminiApiKey ? 'Configured' : 'Not configured'}`);
            console.log('');
            console.log(`🚀 API available at: http://localhost:${config.port}`);
            console.log(`📊 Health check: http://localhost:${config.port}/health`);
            console.log('');
            console.log('Available endpoints:');
            console.log('  POST   /api/auth/register');
            console.log('  POST   /api/auth/login');
            console.log('  GET    /api/auth/profile');
            console.log('  POST   /api/chat/message');
            console.log('  GET    /api/chat/sessions');
            console.log('  POST   /api/budgets');
            console.log('  POST   /api/expenses');
            console.log('  GET    /api/financial/banks');
            console.log('  POST   /api/financial/calculate-emi');
            console.log('');
        });
    } catch (error) {
        console.error('Failed to start server:', error);
        process.exit(1);
    }
};

// Start the server
startServer();

export default app;
