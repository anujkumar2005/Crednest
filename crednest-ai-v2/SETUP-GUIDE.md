# 🚀 CredNest AI v2.0 - Complete Setup Guide

## 📋 Quick Start (Easiest Way)

**Just double-click:** `START.bat`

This will automatically:
1. Start MongoDB
2. Start the backend server
3. Open the frontend in your browser

That's it! 🎉

---

## 🛠️ Manual Setup

### Prerequisites
- ✅ Node.js 18+ installed
- ✅ MongoDB installed (local or Atlas)
- ✅ 16GB RAM (you have this!)
- ✅ RTX 3060 GPU (for AI fine-tuning)

### Step 1: Start MongoDB

**Windows:**
```bash
net start MongoDB
```

**Mac/Linux:**
```bash
sudo systemctl start mongod
```

### Step 2: Start Backend Server

```bash
cd server
npm install  # First time only
npm run dev
```

Server will start on: `http://localhost:5000`

### Step 3: Open Frontend

Open in browser:
```
frontend-pages/index.html
```

Or serve it:
```bash
cd frontend-pages
python -m http.server 8080
```

Then visit: `http://localhost:8080`

---

## 🎨 Features

### **7 Complete Pages:**
1. **Login/Register** - User authentication
2. **Dashboard** - Overview with stats
3. **AI Chat** - Financial assistant
4. **Budgeting** - Budget management
5. **Expenses** - Expense tracking
6. **Loans** - EMI calculator & banks
7. **Investments** - SIP calculator & tips

### **Backend (Node.js/TypeScript):**
- ✅ Express server
- ✅ MongoDB database
- ✅ JWT authentication
- ✅ AI integration
- ✅ All API endpoints

### **Frontend (Multi-Page Dark Theme):**
- ✅ Ultra-dark design
- ✅ Animated backgrounds
- ✅ Smooth transitions
- ✅ Fully responsive
- ✅ No external dependencies

---

## 🤖 AI Model Fine-tuning

### For Custom AI Model (Optional)

Open `model-finetuning.ipynb` in Jupyter Notebook:

```bash
jupyter notebook model-finetuning.ipynb
```

**Optimized for your system:**
- AMD Ryzen 7 5800H
- RTX 3060 6GB VRAM
- 16GB RAM

**Features:**
- 4-bit quantization for memory efficiency
- LoRA for parameter-efficient training
- Financial domain training data
- ~10-15 minutes training time

**Models supported:**
- Mistral-7B
- Llama-2-7B
- Any 7B parameter model

---

## 📁 Project Structure

```
crednest-ai-v2/
├── START.bat                    # One-click startup script
├── server/                      # Backend
│   ├── src/
│   │   ├── config/             # Database & environment
│   │   ├── models/             # Mongoose models
│   │   ├── controllers/        # Request handlers
│   │   ├── routes/             # API routes
│   │   ├── middleware/         # JWT auth
│   │   ├── services/           # AI service
│   │   ├── seeds/              # Database seeds
│   │   └── server.ts           # Main server
│   ├── package.json
│   └── .env                    # Configuration
│
├── frontend-pages/              # Multi-page frontend
│   ├── index.html              # Login/Register
│   ├── css/style.css           # Dark theme CSS
│   ├── js/api.js               # API client
│   └── modules/
│       ├── dashboard.html
│       ├── chat.html
│       ├── budgeting.html
│       ├── expenses.html
│       ├── loans.html
│       └── investments.html
│
├── model-finetuning.ipynb      # AI fine-tuning notebook
├── README.md
├── QUICKSTART.md
└── FRONTEND-COMPLETE.md
```

---

## 🎯 Usage Guide

### 1. Create Account
- Open frontend
- Click "Register" tab
- Enter name, email, password
- Click "Create Account"

### 2. Explore Features

**Dashboard:**
- View budget summary
- See recent expenses
- Quick action cards

**AI Chat:**
- Ask financial questions
- Calculate EMI
- Check loan eligibility
- Get financial tips

**Budgeting:**
- Create monthly budgets
- Track spending by category
- View progress bars

**Expenses:**
- Add expenses with categories
- Track payment methods
- View expense history

**Loans:**
- Calculate EMI
- Check eligibility
- Compare banks
- Filter by loan type

**Investments:**
- Calculate SIP returns
- View investment options
- Risk level guide
- Investment tips

---

## 🔧 Configuration

### Environment Variables (server/.env)

```env
NODE_ENV=development
PORT=5000
MONGODB_URI=mongodb://localhost:27017/crednest_ai
JWT_SECRET=crednest-ai-super-secret-key-2025-v2
JWT_EXPIRE=7d
GEMINI_API_KEY=your_api_key_here
CORS_ORIGIN=http://localhost:3000
```

### Database Seeding

Add sample bank data:
```bash
cd server
npm run seed
```

---

## 📊 API Endpoints

### Authentication
```
POST   /api/auth/register      - Register user
POST   /api/auth/login         - Login user
GET    /api/auth/profile       - Get profile (protected)
PUT    /api/auth/profile       - Update profile (protected)
```

### AI Chat
```
POST   /api/chat/message       - Send message (protected)
GET    /api/chat/sessions      - Get sessions (protected)
GET    /api/chat/history/:id   - Get history (protected)
DELETE /api/chat/session/:id   - Delete session (protected)
```

### Budgets & Expenses
```
POST   /api/budgets            - Create budget (protected)
GET    /api/budgets            - Get budgets (protected)
PUT    /api/budgets/:id        - Update budget (protected)
DELETE /api/budgets/:id        - Delete budget (protected)
GET    /api/budgets/summary    - Get summary (protected)

POST   /api/expenses           - Add expense (protected)
GET    /api/expenses           - Get expenses (protected)
DELETE /api/expenses/:id       - Delete expense (protected)
```

### Financial Services
```
GET    /api/financial/banks           - Get banks (protected)
GET    /api/financial/banks/:id       - Get bank details (protected)
POST   /api/financial/calculate-emi   - Calculate EMI (protected)
POST   /api/financial/check-eligibility - Check eligibility (protected)
```

---

## 🐛 Troubleshooting

### MongoDB Connection Error
```
Error: connect ECONNREFUSED 127.0.0.1:27017
```
**Solution:** Start MongoDB
```bash
net start MongoDB
```

### Port Already in Use
```
Error: listen EADDRINUSE: address already in use :::5000
```
**Solution:** Change port in `.env`
```env
PORT=5001
```

### Frontend Not Loading
**Solution:** Make sure server is running on port 5000

### AI Responses Not Working
**Solution:** Check API key in `server/.env`

---

## 🎨 Customization

### Change Theme Colors

Edit `frontend-pages/css/style.css`:

```css
:root {
    --primary: #6366f1;      /* Change primary color */
    --bg-primary: #0a0a0f;   /* Change background */
    --text-primary: #ffffff;  /* Change text color */
}
```

### Add New Features

1. Create new model in `server/src/models/`
2. Create controller in `server/src/controllers/`
3. Add routes in `server/src/routes/`
4. Create frontend page in `frontend-pages/modules/`

---

## 📈 Performance

**Optimized for RTX 3060:**
- GPU-accelerated animations
- Efficient CSS transforms
- Minimal repaints
- Smooth 60fps

**Backend:**
- TypeScript for type safety
- MongoDB for fast queries
- JWT for stateless auth
- Async/await for performance

---

## 🔒 Security

- ✅ Password hashing (bcrypt)
- ✅ JWT tokens (7-day expiry)
- ✅ CORS protection
- ✅ Helmet security headers
- ✅ Input validation
- ✅ SQL injection protection (MongoDB)

---

## 📝 Development

### Available Scripts

**Backend:**
```bash
npm run dev      # Start development server
npm run build    # Build TypeScript
npm start        # Start production server
npm run seed     # Seed database
```

**Frontend:**
- No build required! Pure HTML/CSS/JS

---

## 🚀 Deployment

### Backend (Node.js)
- Deploy to Heroku, Railway, or Render
- Set environment variables
- Connect to MongoDB Atlas

### Frontend
- Deploy to Netlify, Vercel, or GitHub Pages
- Update API_URL in `js/api.js`

---

## 📄 License

MIT License - Free to use for personal and commercial projects

---

## 🎉 You're All Set!

**Double-click `START.bat` and enjoy your financial platform!**

For questions or issues, check the documentation files:
- `README.md` - Main documentation
- `QUICKSTART.md` - Quick setup guide
- `FRONTEND-COMPLETE.md` - Frontend details

**Happy Coding! 💰🚀**
