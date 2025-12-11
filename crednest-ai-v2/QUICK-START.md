# 🚀 Quick Start Guide - CredNest AI

## Step 1: Start MongoDB

**Option A: Using MongoDB Compass (What you're doing now)**
1. The connection string is correct: `mongodb://localhost:27017/`
2. MongoDB service needs to be running first
3. Open **Command Prompt as Administrator**
4. Run: `net start MongoDB`
5. Then click "Connect" in Compass

**Option B: Check if MongoDB is already running**
```bash
# Open Command Prompt (regular, not admin)
mongosh
# If it connects, MongoDB is running!
```

**Option C: Start MongoDB manually**
```bash
# Navigate to MongoDB bin folder
cd "C:\Program Files\MongoDB\Server\7.0\bin"
mongod --dbpath "C:\data\db"
```

## Step 2: Start the Backend Server

```bash
cd d:\crednest-ai\crednest-ai-v2\server
npm install  # First time only
npm run dev
```

Server will start on: `http://localhost:5000`

## Step 3: Open Frontend

```
Open: d:\crednest-ai\crednest-ai-v2\frontend-pages\index.html
```

## Step 4: AI Fine-tuning (Optional)

**Training data is ready!** ✅ 27 examples generated

```bash
# Install Jupyter
pip install jupyter

# Open notebook
cd d:\crednest-ai\crednest-ai-v2
jupyter notebook model-finetuning.ipynb
```

---

## ✅ Training Data Generated!

Your AI training dataset is ready with:
- **27 comprehensive examples**
- Real bank loan data (SBI, HDFC, ICICI, Axis, PNB)
- Actual interest rates & schemes
- Government programs (PMAY)
- EMI calculations
- Tax planning
- Investment advice

File location: `server/complete_financial_training.json`

---

## 🔧 Troubleshooting

### MongoDB won't start?
1. Open Command Prompt **as Administrator**
2. Run: `net start MongoDB`
3. If error, MongoDB might not be installed
4. Download from: https://www.mongodb.com/try/download/community

### Can't connect in Compass?
- Make sure MongoDB service is running
- Use connection string: `mongodb://localhost:27017/`
- Click "Save & Connect"

### Backend won't start?
```bash
cd server
npm install
npm run dev
```

---

## 📊 What's Next?

1. ✅ **MongoDB Connected** - Use Compass to view data
2. ✅ **Training Data Ready** - 27 examples in JSON
3. ⏳ **Start Backend** - Run `npm run dev`
4. ⏳ **Open Frontend** - Test all features
5. ⏳ **Fine-tune AI** - Run Jupyter notebook

**You're almost there!** 🎉
