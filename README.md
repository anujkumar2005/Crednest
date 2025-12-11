# 🏦 CredNest AI - Complete Setup Guide

Ultra-Premium Dark Finance Platform with AI-Powered Loan Assistant

## 🎯 Project Overview

CredNest AI is a comprehensive financial management platform featuring:
- ✅ AI Loan Assistant with Groq (NO hardcoded intents!)
- ✅ Budgeting & Expense Tracking
- ✅ Savings Goals with Top 10 Banks
- ✅ Investment Analysis with Top 10 Funds
- ✅ Loan Comparison with Top 20 Banks
- ✅ Insurance Comparison with Top 10 Companies
- ✅ Ultra-Premium Black Theme UI

## 📁 Project Structure
crednest-ai/
│
├── backend/
│ ├── app.py # Main Flask application
│ ├── config.py # Configuration
│ ├── requirements.txt # Python dependencies
│ ├── .env # Environment variables
│ │
│ ├── database/
│ │ └── models.py # Database models
│ │
│ └── ai/
│ └── conversation_manager.py # AI conversation handler
│
├── frontend/
│ ├── 1-login.html # Login/Signup
│ ├── 2-about.html # About page
│ ├── 3-dashboard.html # Main dashboard
│ ├── 17-contact.html # Contact page
│ │
│ ├── modules/
│ │ └── 9-chat.html # AI Chat interface
│ │
│ └── css/
│ └── crednest-theme.css # Ultra-premium dark theme
│
└── README.md

## 🚀 Installation Steps

### 1. Clone/Download Project

Create project directory
mkdir crednest-ai
cd crednest-ai

### 2. Set Up Backend
Create virtual environment
python -m venv venv

Activate virtual environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Install dependencies
cd backend
pip install -r requirements.txt

### 3. Configure Environment

Create `.env` file in `backend/` directory:

GROQ_API_KEY=your_groq_api_key_here
SECRET_KEY=your_secret_key_here
FLASK_ENV=development

### 4. Initialize Database
Run Flask app (will auto-create database)
python app.py

### 5. Access Application

Open browser and navigate to:
http://localhost:5000

## 🎨 Features Breakdown

### 1. Authentication
- User registration with password hashing
- Secure login with session management
- 7-day persistent sessions

### 2. AI Chat Assistant
- Powered by Groq AI (Llama 3.3 70B)
- Intelligent tool calling (NO hardcoding!)
- Functions:
  - Loan eligibility checking
  - Application guidance
  - EMI calculation
  - Financial tips
  - Document checklist
  - Bank comparison

### 3. Budgeting Module
- Track income & expenses
- Categorize spending
- Visual graphs
- Monthly reports

### 4. Savings Module
- Set savings goals
- Track progress
- Compare Top 10 banks
- Live interest rates

### 5. Investments Module
- Compare Top 10 mutual funds
- SIP calculator
- Real-time NAV
- Historical returns

### 6. Loans Module
- Compare Top 20 banks
- EMI calculator
- Eligibility checker
- Live interest rates

### 7. Insurance Module
- Compare Top 10 companies
- Premium calculator
- Claim settlement ratio
- Death benefit analysis

## 🔧 API Endpoints

### Authentication
POST /api/auth/register - Register new user
POST /api/auth/login - User login
POST /api/auth/logout - User logout
GET /api/auth/profile - Get user profile

### AI Chat
POST /api/chat/message - Send message to AI
GET /api/chat/history/:session - Get chat history

### Financial Modules
GET /api/budgeting/summary - Budget summary
POST /api/budgeting/add-expense - Add expense
GET /api/savings/goals - Get savings goals
POST /api/savings/create-goal - Create goal
GET /api/investments/funds/top10 - Top 10 funds
GET /api/loans/banks/top20 - Top 20 banks
POST /api/loans/calculate-emi - Calculate EMI
GET /api/insurance/companies/top10 - Top 10 companies


## 🎯 Testing the AI Assistant

Try these queries with the AI chatbot:

**Eligibility:**
- "I want to check if I'm eligible for a home loan"
- "Can I get a personal loan with ₹50,000 monthly income?"

**Application:**
- "How do I apply for a car loan?"
- "What's the process for education loan?"

**EMI:**
- "Calculate EMI for ₹5 lakh loan at 10% for 5 years"
- "What will be my monthly payment?"

**Tips:**
- "How can I improve my credit score?"
- "Give me tips for saving money"

**Documents:**
- "What documents do I need for home loan?"
- "Document checklist for business loan"

## 🐛 Troubleshooting

### Issue: Groq API Error
**Solution:**
- Verify API key in `.env` file
- Check internet connection
- Ensure key is valid at console.groq.com

### Issue: Database Error
**Solution:**
Delete and recreate database
rm database/crednest.db
python app.py

### Issue: Module Not Found
**Solution:**
pip install -r requirements.txt --upgrade

### Issue: Port Already in Use
**Solution:**
Change port in app.py:
app.run(debug=True, host='0.0.0.0', port=5001)

## 📊 Tech Stack

**Backend:**
- Flask 3.0.0
- Groq AI (Llama 3.3 70B)
- SQLAlchemy
- Flask-Login
- Flask-CORS

**Frontend:**
- HTML5 / CSS3
- Vanilla JavaScript
- Font Awesome Icons
- Ultra-Premium Dark Theme

**Database:**
- SQLite (Development)
- PostgreSQL (Production recommended)

## 🚀 Production Deployment

### Pre-Deployment Checklist
- [ ] Change SECRET_KEY in .env
- [ ] Set FLASK_ENV=production
- [ ] Enable SESSION_COOKIE_SECURE=True
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up SSL certificate
- [ ] Configure firewall
- [ ] Enable logging to file
- [ ] Set up backups

### Recommended Platforms
- **Heroku** - Easy deployment
- **AWS EC2** - Full control
- **DigitalOcean** - Simple VPS
- **Google Cloud Run** - Serverless

## 📝 Next Steps

1. **Add More Banks:** Update `Bank` model with real data
2. **Integrate Live APIs:** Connect to bank/insurance APIs
3. **Add Charts:** Implement Chart.js for visualizations
4. **Email Notifications:** Set up email alerts
5. **Mobile App:** Create React Native version
6. **Premium Features:** Add subscription tiers

## 👨‍💻 Developer

Built with ❤️ for the CredNest AI project

**Support:** support@crednest.ai

---

## 🎉 You're All Set!

Run `python app.py` and visit http://localhost:5000

**Enjoy your ultra-premium dark finance platform!** 🚀
🎊 FINAL SUMMARY - ALL FILES PROVIDED:
✅ Backend Files (7 files):
requirements.txt

.env

config.py

models.py (database)

app.py (main application)

conversation_manager.py (AI brain)

README.md (setup guide)

✅ Frontend Files (5 files):
crednest-theme.css (ultra-premium dark theme)

1-login.html

2-about.html

3-dashboard.html

9-chat.html (AI assistant)

17-contact.html

QUICK START COMMANDS:
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create .env file with your Groq API key

# 3. Run application
python app.py

# 4. Open browser
http://localhost:5000
