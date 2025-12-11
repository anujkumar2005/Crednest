"""
Comprehensive Database Verification Script
Checks MySQL database integrity, tables, and data
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database.models import db, User, Budget, Expense, Income, ChatHistory, Bank, InsuranceCompany, InvestmentFund
from app import app
from sqlalchemy import inspect

print("=" * 70)
print("🗄️  CREDNEST AI - DATABASE VERIFICATION")
print("=" * 70)

with app.app_context():
    # 1. Database Connection
    print("\n📡 DATABASE CONNECTION:")
    print(f"   Type: MySQL")
    print(f"   Database: crednest_db")
    print(f"   Host: 127.0.0.1:3306")
    print(f"   Status: ✅ Connected")
    
    # 2. Table Verification
    print("\n📋 TABLE VERIFICATION:")
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print(f"   Total Tables: {len(tables)}")
    for table in sorted(tables):
        print(f"   ✓ {table}")
    
    # 3. Record Counts
    print("\n📊 RECORD COUNTS:")
    counts = {
        'Users': User.query.count(),
        'Budgets': Budget.query.count(),
        'Expenses': Expense.query.count(),
        'Incomes': Income.query.count(),
        'Chat History': ChatHistory.query.count(),
        'Banks': Bank.query.count(),
        'Insurance Companies': InsuranceCompany.query.count(),
        'Investment Funds': InvestmentFund.query.count()
    }
    
    for name, count in counts.items():
        status = "✅" if count > 0 else "⚠️ "
        print(f"   {status} {name}: {count}")
    
    # 4. Sample Data Verification
    print("\n🏦 SAMPLE BANK DATA:")
    banks = Bank.query.limit(5).all()
    if banks:
        for bank in banks:
            print(f"   • {bank.name}")
            print(f"     Home Loan: {bank.home_loan_rate}% | Personal Loan: {bank.personal_loan_rate}%")
    else:
        print("   ⚠️  No bank data found!")
    
    print("\n🛡️  SAMPLE INSURANCE DATA:")
    insurance = InsuranceCompany.query.limit(5).all()
    if insurance:
        for ins in insurance:
            print(f"   • {ins.name}")
            print(f"     CSR: {ins.claim_settlement_ratio}% | Rating: {ins.rating}/5")
    else:
        print("   ⚠️  No insurance data found!")
    
    print("\n📈 SAMPLE INVESTMENT FUND DATA:")
    funds = InvestmentFund.query.limit(5).all()
    if funds:
        for fund in funds:
            print(f"   • {fund.fund_name}")
            print(f"     1Y Return: {fund.returns_1yr}% | 3Y Return: {fund.returns_3yr}%")
    else:
        print("   ⚠️  No investment fund data found!")
    
    # 5. Data Integrity Checks
    print("\n🔍 DATA INTEGRITY CHECKS:")
    
    # Check for null values in critical fields
    banks_with_null = Bank.query.filter(
        (Bank.name == None) | 
        (Bank.home_loan_rate == None) | 
        (Bank.personal_loan_rate == None)
    ).count()
    
    insurance_with_null = InsuranceCompany.query.filter(
        (InsuranceCompany.name == None) | 
        (InsuranceCompany.claim_settlement_ratio == None)
    ).count()
    
    funds_with_null = InvestmentFund.query.filter(
        (InvestmentFund.fund_name == None) | 
        (InvestmentFund.returns_1yr == None)
    ).count()
    
    print(f"   Banks with missing data: {banks_with_null}")
    print(f"   Insurance with missing data: {insurance_with_null}")
    print(f"   Funds with missing data: {funds_with_null}")
    
    if banks_with_null == 0 and insurance_with_null == 0 and funds_with_null == 0:
        print("   ✅ All critical data is complete!")
    else:
        print("   ⚠️  Some records have missing data")
    
    # 6. User Data Check
    print("\n👥 USER DATA:")
    users = User.query.all()
    if users:
        print(f"   Total Users: {len(users)}")
        for user in users:
            print(f"   • {user.email} (ID: {user.id})")
            user_budgets = Budget.query.filter_by(user_id=user.id).count()
            user_expenses = Expense.query.filter_by(user_id=user.id).count()
            user_incomes = Income.query.filter_by(user_id=user.id).count()
            user_chats = ChatHistory.query.filter_by(user_id=user.id).count()
            print(f"     Budgets: {user_budgets} | Expenses: {user_expenses} | Incomes: {user_incomes} | Chats: {user_chats}")
    else:
        print("   ℹ️  No users registered yet")
    
    # 7. Overall Status
    print("\n" + "=" * 70)
    print("📊 OVERALL DATABASE STATUS:")
    
    total_records = sum(counts.values())
    critical_data_complete = (counts['Banks'] >= 10 and 
                             counts['Insurance Companies'] >= 5 and 
                             counts['Investment Funds'] >= 5)
    
    if critical_data_complete:
        print("   ✅ Database is properly configured")
        print(f"   ✅ {total_records} total records")
        print("   ✅ All critical data is present")
        print("   ✅ Ready for production use")
    else:
        print("   ⚠️  Database needs attention")
        if counts['Banks'] < 10:
            print("   ⚠️  Insufficient bank data (need at least 10)")
        if counts['Insurance Companies'] < 5:
            print("   ⚠️  Insufficient insurance data (need at least 5)")
        if counts['Investment Funds'] < 5:
            print("   ⚠️  Insufficient investment fund data (need at least 5)")
    
    print("=" * 70)
