# CredNest AI v2.0 - Node.js/TypeScript Edition

> Complete financial management platform with Google Gemini AI

## 🎯 Overview

CredNest AI v2.0 is a complete rebuild of the financial platform using modern technologies:

- **Backend**: Node.js + Express + TypeScript
- **Database**: MongoDB
- **AI**: Google Gemini AI
- **Frontend**: React + TypeScript (coming soon)
- **Auth**: JWT-based authentication

## 🚀 Features

- ✅ User authentication with JWT
- ✅ AI-powered financial assistant (Gemini)
- ✅ Budget management
- ✅ Expense tracking
- ✅ Loan calculator & eligibility checker
- ✅ Bank comparison (Top 10 Indian banks)
- ✅ EMI calculator
- ✅ Chat history with sessions

## 📁 Project Structure

```
crednest-ai-v2/
├── server/                 # Backend (Node.js/TypeScript)
│   ├── src/
│   │   ├── config/        # Configuration files
│   │   ├── models/        # Mongoose models
│   │   ├── controllers/   # Request handlers
│   │   ├── routes/        # API routes
│   │   ├── middleware/    # Auth & error handling
│   │   ├── services/      # Gemini AI service
│   │   ├── seeds/         # Database seed data
│   │   └── server.ts      # Main server file
│   ├── package.json
│   ├── tsconfig.json
│   └── .env
│
└── client/                # Frontend (React - Coming Soon)
```

## 🛠️ Installation

### Prerequisites

- Node.js 18+ and npm
- MongoDB (local or Atlas)
- Google Gemini API key

### Backend Setup

1. **Navigate to server directory**
```bash
cd crednest-ai-v2/server
```

2. **Install dependencies**
```bash
npm install
```

3. **Configure environment**

The `.env` file is already created with your Gemini API key:
```env
NODE_ENV=development
PORT=5000
MONGODB_URI=mongodb://localhost:27017/crednest_ai
JWT_SECRET=crednest-ai-super-secret-key-2025-v2
JWT_EXPIRE=7d
GEMINI_API_KEY=AIzaSyBQfaLRLgHmed1SeDeolZjMzlwswBseMuM
CORS_ORIGIN=http://localhost:3000
```

4. **Start MongoDB**

If using local MongoDB:
```bash
# Windows
net start MongoDB

# Mac/Linux
sudo systemctl start mongod
```

Or use MongoDB Atlas (cloud) - update `MONGODB_URI` in `.env`

5. **Seed database** (optional - adds bank data)
```bash
npm run seed
```

6. **Start development server**
```bash
npm run dev
```

Server will start on http://localhost:5000

## 📡 API Endpoints

### Authentication
```
POST   /api/auth/register      - Register new user
POST   /api/auth/login         - Login user
GET    /api/auth/profile       - Get user profile (protected)
PUT    /api/auth/profile       - Update profile (protected)
```

### AI Chat
```
POST   /api/chat/message       - Send message to AI (protected)
GET    /api/chat/sessions      - Get all chat sessions (protected)
GET    /api/chat/history/:id   - Get session history (protected)
DELETE /api/chat/session/:id   - Delete session (protected)
```

### Budget & Expenses
```
POST   /api/budgets            - Create budget (protected)
GET    /api/budgets            - Get budgets (protected)
PUT    /api/budgets/:id        - Update budget (protected)
DELETE /api/budgets/:id        - Delete budget (protected)
GET    /api/budgets/summary    - Get budget summary (protected)

POST   /api/expenses           - Add expense (protected)
GET    /api/expenses           - Get expenses (protected)
DELETE /api/expenses/:id       - Delete expense (protected)
```

### Financial Services
```
GET    /api/financial/banks           - Get banks list (protected)
GET    /api/financial/banks/:id       - Get bank details (protected)
POST   /api/financial/calculate-emi   - Calculate EMI (protected)
POST   /api/financial/check-eligibility - Check loan eligibility (protected)
```

## 🧪 Testing the API

### 1. Register a user
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "name": "Test User"
  }'
```

### 2. Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

Save the `token` from response.

### 3. Chat with AI
```bash
curl -X POST http://localhost:5000/api/chat/message \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "message": "Calculate EMI for 5 lakh loan at 10% for 5 years"
  }'
```

### 4. Get Banks
```bash
curl -X GET http://localhost:5000/api/financial/banks \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## 🤖 Gemini AI Features

The AI assistant can:

1. **Calculate EMI** - Automatically detects loan amounts, rates, and tenure
2. **Check Loan Eligibility** - Analyzes income and loan amount
3. **Provide Financial Tips** - Advice on saving, investing, budgeting, etc.
4. **General Financial Advice** - Answers questions about finance

Example queries:
- "Calculate EMI for ₹5 lakh at 10% for 5 years"
- "Am I eligible for a loan of 10 lakhs with 50k monthly income?"
- "Give me tips for saving money"
- "How can I improve my credit score?"

## 🔧 Development

### Available Scripts

```bash
npm run dev      # Start development server with hot reload
npm run build    # Build TypeScript to JavaScript
npm start        # Start production server
npm run seed     # Seed database with bank data
```

### Tech Stack

- **Runtime**: Node.js 18+
- **Framework**: Express.js
- **Language**: TypeScript
- **Database**: MongoDB with Mongoose
- **AI**: Google Gemini AI
- **Auth**: JWT (jsonwebtoken)
- **Security**: Helmet, bcryptjs
- **Logging**: Morgan

## 📝 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `NODE_ENV` | Environment mode | `development` |
| `PORT` | Server port | `5000` |
| `MONGODB_URI` | MongoDB connection string | `mongodb://localhost:27017/crednest_ai` |
| `JWT_SECRET` | JWT signing secret | Required |
| `JWT_EXPIRE` | Token expiration | `7d` |
| `GEMINI_API_KEY` | Google Gemini API key | Required |
| `CORS_ORIGIN` | Allowed CORS origin | `http://localhost:3000` |

## 🚧 Coming Soon

- [ ] React frontend with Material-UI
- [ ] Investment fund comparison
- [ ] Insurance comparison
- [ ] Savings goals tracking
- [ ] Advanced analytics dashboard
- [ ] Email notifications
- [ ] PDF report generation

## 🐛 Troubleshooting

### MongoDB Connection Error
```bash
# Make sure MongoDB is running
# Windows: net start MongoDB
# Mac/Linux: sudo systemctl start mongod

# Or use MongoDB Atlas and update MONGODB_URI
```

### Port Already in Use
```bash
# Change PORT in .env file
PORT=5001
```

### Gemini API Error
```bash
# Verify API key is correct in .env
# Check quota at: https://makersuite.google.com/app/apikey
```

## 📄 License

MIT License - feel free to use for your projects!

## 👨‍💻 Developer

Built by Anuj with ❤️

---

**Happy Coding! 🚀**
