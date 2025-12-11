# CredNest AI - MySQL Database Setup Guide

## 🗄️ Database Migration: SQLite → MySQL

This guide will help you set up MySQL database for CredNest AI.

---

## Prerequisites

### 1. Install MySQL

**Windows:**
- Download MySQL Installer from: https://dev.mysql.com/downloads/installer/
- Run installer and select "MySQL Server" + "MySQL Workbench"
- Set root password during installation
- Default port: 3306

**Verify Installation:**
```bash
mysql --version
```

---

## Step-by-Step Setup

### Step 1: Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

**New dependencies added:**
- `PyMySQL` - MySQL connector for Python
- `cryptography` - Required by PyMySQL

---

### Step 2: Configure Database Settings

Edit `backend/.env` file:

```bash
# Database Configuration (MySQL)
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=crednest_db
DB_USER=root
DB_PASSWORD=your_mysql_password_here
DB_CHARSET=utf8mb4
```

**Important:** Replace `your_mysql_password_here` with your actual MySQL root password!

---

### Step 3: Create MySQL Database

**Option A: Using Python Script**
```bash
cd backend/database
python db_config.py
```

This will automatically create the `crednest_db` database.

**Option B: Manual Creation**
```sql
CREATE DATABASE crednest_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

### Step 4: Initialize Database Tables

```bash
cd backend
python app.py
```

The application will automatically:
1. Connect to MySQL
2. Create all tables (users, budgets, expenses, incomes, chat_history, banks, etc.)
3. Seed initial data (banks, insurance companies, investment funds)

---

## Database Schema

### User Tables (Per-User Data)

#### **users** - User profiles
- id, email, password_hash
- name, age, gender, date_of_birth, phone
- address, city, state, country, pincode
- occupation, company, monthly_income
- profile_image, bio, profile_completed
- is_active, is_verified
- created_at, last_login, updated_at

#### **budgets** - Monthly budgets
- id, user_id, month, category
- planned_amount, spent_amount
- icon, color, notes, is_active
- created_at, updated_at

#### **expenses** - Daily expenses
- id, user_id, budget_id
- amount, category, description, date
- payment_method, location
- tags, notes
- is_recurring, recurring_frequency
- receipt_url
- created_at, updated_at

#### **incomes** - Income tracking
- id, user_id, month
- source, amount, description
- is_recurring, received_date
- created_at, updated_at

#### **chat_history** - AI conversations
- id, user_id, session_id
- message, response
- tool_used, response_time
- created_at

### Reference Tables (Shared Data)

#### **banks** - Top 20 banks
- Loan rates, savings rates, FD rates
- Processing fees, loan ranges
- Customer support, ratings

#### **insurance_companies** - Top 10 insurers
- Premium rates (life, health, car)
- Claim settlement ratio
- Coverage details

#### **investment_funds** - Top 10 funds
- NAV, returns (1yr, 3yr, 5yr)
- Expense ratio, risk level
- Minimum investment amounts

---

## Viewing Database

### Option 1: Database Viewer (Built-in)

Access the web-based database viewer:
```
http://localhost:5000/admin/db-viewer
```

Features:
- View all tables
- Filter by user ID
- Pagination support
- Export to CSV
- Real-time stats

### Option 2: MySQL Workbench

1. Open MySQL Workbench
2. Connect to localhost:3306
3. Select `crednest_db` database
4. Browse tables visually

### Option 3: Command Line

```bash
mysql -u root -p
USE crednest_db;
SHOW TABLES;
SELECT * FROM users;
SELECT * FROM budgets WHERE user_id = 1;
```

---

## Data Isolation

**Every user's data is completely isolated:**

✅ All queries automatically filter by `user_id`
✅ Foreign key constraints ensure data integrity
✅ Cascade delete removes all user data on account deletion
✅ No user can access another user's data

**Example:**
```python
# User 1's budgets
Budget.query.filter_by(user_id=1).all()

# User 2's budgets  
Budget.query.filter_by(user_id=2).all()

# Results are completely separate!
```

---

## API Endpoints

### Profile Management
- `PUT /api/profile/update` - Update user profile
- `GET /api/auth/profile` - Get profile

### Budget Management
- `POST /api/budgets/create` - Create monthly budget
- `GET /api/budgets/month/<YYYY-MM>` - Get monthly budget
- `PUT /api/budgets/<id>` - Update budget
- `DELETE /api/budgets/<id>` - Delete budget

### Expense Management
- `POST /api/expenses/add` - Add expense
- `GET /api/expenses?month=YYYY-MM&category=Food` - Get expenses
- `PUT /api/expenses/<id>` - Update expense
- `DELETE /api/expenses/<id>` - Delete expense

### Income Management
- `POST /api/income/add` - Add income
- `GET /api/income?month=YYYY-MM` - Get income
- `PUT /api/income/<id>` - Update income
- `DELETE /api/income/<id>` - Delete income

### Database Viewer (Admin)
- `GET /admin/db-viewer` - Database viewer page
- `GET /api/database/stats` - Get database statistics
- `GET /api/database/table/<table_name>` - Get table data

---

## Troubleshooting

### Error: "Access denied for user 'root'@'localhost'"
**Solution:** Check DB_PASSWORD in .env file

### Error: "Unknown database 'crednest_db'"
**Solution:** Run `python database/db_config.py` to create database

### Error: "No module named 'pymysql'"
**Solution:** Run `pip install -r requirements.txt`

### Error: "Can't connect to MySQL server"
**Solution:** 
1. Check if MySQL service is running
2. Verify DB_HOST and DB_PORT in .env
3. Check firewall settings

---

## Backup & Restore

### Create Backup
```bash
mysqldump -u root -p crednest_db > backup.sql
```

### Restore Backup
```bash
mysql -u root -p crednest_db < backup.sql
```

---

## Production Deployment

### Security Checklist
- [ ] Change DB_PASSWORD to strong password
- [ ] Use environment variables (don't commit .env)
- [ ] Enable MySQL SSL connections
- [ ] Set up regular backups
- [ ] Configure firewall rules
- [ ] Use separate database user (not root)
- [ ] Enable query logging for auditing

### Performance Optimization
- [ ] Add indexes on frequently queried columns
- [ ] Enable query caching
- [ ] Configure connection pooling
- [ ] Monitor slow queries
- [ ] Set up database replication (if needed)

---

## Switching Back to SQLite

If you want to switch back to SQLite:

1. Edit `.env`:
```bash
DB_TYPE=sqlite
```

2. Restart application - it will automatically use SQLite

---

## Summary

✅ **MySQL Database** - Production-ready SQL database
✅ **Enhanced User Profiles** - Age, gender, address, occupation, income
✅ **Complete Budgeting System** - Income tracking, expense management
✅ **Data Isolation** - Each user's data is completely separate
✅ **Database Viewer** - Built-in web interface to view all tables
✅ **Production Ready** - Proper indexing, relationships, and constraints

Your CredNest AI is now running on a professional MySQL database! 🚀
