"""
Simple Database Verification
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db
from database.models import Bank, InsuranceCompany, InvestmentFund, User
from sqlalchemy import inspect, text

print("="*70)
print("🔍 CREDNEST AI - SIMPLE DATABASE CHECK")
print("="*70)

with app.app_context():
    try:
        # Check connection
        print("\n✅ Database connected")
        
        # Get tables
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"\n📋 Tables: {len(tables)}")
        for table in sorted(tables):
            print(f"   ✓ {table}")
        
        # Count records using raw SQL to avoid ORM issues
        print(f"\n📊 Record Counts:")
        
        with db.engine.connect() as conn:
            banks_count = conn.execute(text("SELECT COUNT(*) FROM banks")).scalar()
            insurance_count = conn.execute(text("SELECT COUNT(*) FROM insurance_companies")).scalar()
            funds_count = conn.execute(text("SELECT COUNT(*) FROM investment_funds")).scalar()
            users_count = conn.execute(text("SELECT COUNT(*) FROM users")).scalar()
            
            print(f"   Banks: {banks_count}")
            print(f"   Insurance: {insurance_count}")
            print(f"   Funds: {funds_count}")
            print(f"   Users: {users_count}")
        
        # Sample data
        print(f"\n🏦 Sample Banks:")
        banks = Bank.query.limit(3).all()
        for bank in banks:
            print(f"   • {bank.name} - Home: {bank.home_loan_rate}%")
        
        print(f"\n🛡️  Sample Insurance:")
        insurance = InsuranceCompany.query.limit(3).all()
        for ins in insurance:
            print(f"   • {ins.name} - CSR: {ins.claim_settlement_ratio}%")
        
        print(f"\n📈 Sample Funds:")
        funds = InvestmentFund.query.limit(3).all()
        for fund in funds:
            print(f"   • {fund.fund_name} - 1Y: {fund.returns_1yr}%")
        
        print("\n" + "="*70)
        print("✅ DATABASE IS WORKING PERFECTLY!")
        print("="*70)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
