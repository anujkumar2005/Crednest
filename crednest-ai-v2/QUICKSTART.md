# 🚀 Quick Start Guide - CredNest AI v2.0

## Prerequisites Check

Before starting, make sure you have:
- ✅ Node.js 18+ installed (`node --version`)
- ✅ MongoDB installed or MongoDB Atlas account
- ✅ Google Gemini API key (already configured)

## Step-by-Step Setup

### 1. Start MongoDB

**Option A: Local MongoDB**
```bash
# Windows
net start MongoDB

# Mac
brew services start mongodb-community

# Linux
sudo systemctl start mongod
```

**Option B: MongoDB Atlas (Cloud)**
- Sign up at https://www.mongodb.com/cloud/atlas
- Create a free cluster
- Get connection string
- Update `MONGODB_URI` in `server/.env`

### 2. Install Dependencies

```bash
cd crednest-ai-v2/server
npm install
```

### 3. Seed Database (Optional)

Add sample bank data:
```bash
npm run seed
```

### 4. Start Server

```bash
npm run dev
```

You should see:
```
╔════════════════════════════════════════════════════════════╗
║              🏦 CredNest AI Server v2.0                   ║
╚════════════════════════════════════════════════════════════╝

✓ MongoDB Connected: localhost
✓ Server running on port 5000
✓ Gemini AI: Configured
```

### 5. Test the API

**Health Check:**
```bash
curl http://localhost:5000/health
```

**Register User:**
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\",\"name\":\"Test User\"}"
```

**Login:**
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"
```

Save the `token` from the response!

**Chat with AI:**
```bash
curl -X POST http://localhost:5000/api/chat/message \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d "{\"message\":\"Calculate EMI for 5 lakh loan at 10% for 5 years\"}"
```

## 🎯 What's Working

✅ **Backend (Node.js/TypeScript)**
- Express server with TypeScript
- MongoDB database with Mongoose
- JWT authentication
- Google Gemini AI integration
- All API endpoints functional

✅ **Features**
- User registration & login
- AI chat with tool calling
- Budget management
- Expense tracking
- EMI calculator
- Loan eligibility checker
- Bank comparison

## 📁 Project Structure

```
crednest-ai-v2/
├── server/
│   ├── src/
│   │   ├── config/          # Database & environment
│   │   ├── models/          # User, Chat, Budget, Expense, Bank
│   │   ├── controllers/     # Auth, Chat, Budget, Financial
│   │   ├── routes/          # API routes
│   │   ├── middleware/      # JWT auth
│   │   ├── services/        # Gemini AI service
│   │   ├── seeds/           # Database seeds
│   │   └── server.ts        # Main server
│   ├── package.json
│   ├── tsconfig.json
│   └── .env                 # Configuration
└── README.md
```

## 🔧 Available Commands

```bash
npm run dev      # Start development server (with hot reload)
npm run build    # Build TypeScript to JavaScript
npm start        # Start production server
npm run seed     # Seed database with banks
```

## 🤖 Testing Gemini AI

Try these queries:

1. **EMI Calculation:**
   - "Calculate EMI for ₹5 lakh at 10% for 5 years"
   - "What's the monthly payment for 10 lakh loan at 8.5% for 10 years?"

2. **Loan Eligibility:**
   - "Am I eligible for 10 lakh loan with 50k monthly income?"
   - "Check eligibility for 5 lakh with 40k income"

3. **Financial Tips:**
   - "Give me tips for saving money"
   - "How can I improve my credit score?"
   - "Advice for investing"

## 🐛 Troubleshooting

### MongoDB Connection Error
```
Error: connect ECONNREFUSED 127.0.0.1:27017
```
**Solution:** Make sure MongoDB is running
```bash
# Windows
net start MongoDB

# Mac/Linux
sudo systemctl start mongod
```

### Port Already in Use
```
Error: listen EADDRINUSE: address already in use :::5000
```
**Solution:** Change port in `.env`
```env
PORT=5001
```

### Gemini API Error
```
Error: API key not valid
```
**Solution:** Verify API key in `.env` file

## 📊 API Endpoints Summary

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/auth/register` | Register user | No |
| POST | `/api/auth/login` | Login user | No |
| GET | `/api/auth/profile` | Get profile | Yes |
| POST | `/api/chat/message` | Chat with AI | Yes |
| GET | `/api/chat/sessions` | Get chat sessions | Yes |
| POST | `/api/budgets` | Create budget | Yes |
| GET | `/api/budgets` | Get budgets | Yes |
| POST | `/api/expenses` | Add expense | Yes |
| GET | `/api/financial/banks` | Get banks | Yes |
| POST | `/api/financial/calculate-emi` | Calculate EMI | Yes |

## 🎉 Next Steps

1. ✅ Backend is complete and working
2. 🔄 Frontend (React) - Coming next
3. 🔄 Advanced features (investments, insurance)
4. 🔄 Deployment guide

## 💡 Tips

- Use Postman or Thunder Client for easier API testing
- Check `server/src/server.ts` for all available endpoints
- MongoDB Compass is great for viewing database
- Logs show all API calls in development mode

---

**Server Status:** ✅ Ready to use!

**Need help?** Check the main README.md for detailed documentation.
