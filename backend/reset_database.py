"""
CredNest AI - Complete Database Reset and Initialization
Drops existing database, recreates it, and seeds with data
"""

import pymysql
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def drop_and_create_database():
    """Drop existing database and create fresh one"""
    try:
        print("\n" + "="*70)
        print("🗄️  STEP 1: Database Reset")
        print("="*70)
        
        # Connect to MySQL server
        connection = pymysql.connect(
            host=os.getenv('DB_HOST', '127.0.0.1'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        db_name = os.getenv('DB_NAME', 'crednest_db')
        
        print(f"\n📌 Target Database: {db_name}")
        print(f"📌 MySQL Host: {os.getenv('DB_HOST', '127.0.0.1')}:{os.getenv('DB_PORT', 3306)}")
        
        # Drop database if exists
        print(f"\n🗑️  Dropping existing database '{db_name}'...")
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        print(f"   ✓ Database dropped")
        
        # Create fresh database
        print(f"\n🆕 Creating fresh database '{db_name}'...")
        cursor.execute(f"CREATE DATABASE {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print(f"   ✓ Database created")
        
        cursor.close()
        connection.close()
        
        print("\n✅ Database reset completed successfully!")
        return True
        
    except pymysql.Error as e:
        print(f"\n❌ MySQL Error: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def initialize_tables():
    """Initialize all database tables"""
    try:
        print("\n" + "="*70)
        print("📋 STEP 2: Initialize Tables")
        print("="*70)
        
        from app import app, db
        from sqlalchemy import inspect
        
        with app.app_context():
            print("\n🔨 Creating all tables...")
            db.create_all()
            
            # Get table names
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"\n✅ Created {len(tables)} tables:")
            for table in sorted(tables):
                # Get column count
                columns = inspector.get_columns(table)
                print(f"   ✓ {table:<25} ({len(columns)} columns)")
            
        return True
        
    except Exception as e:
        print(f"\n❌ Error creating tables: {e}")
        import traceback
        traceback.print_exc()
        return False


def seed_database():
    """Seed database with financial data"""
    try:
        print("\n" + "="*70)
        print("🌱 STEP 3: Seed Database")
        print("="*70)
        
        from app import app, db
        from database.models import Bank, InsuranceCompany, InvestmentFund
        from database.seed_data import seed_all_data
        
        with app.app_context():
            print("\n📊 Seeding financial data...")
            success = seed_all_data(db, Bank, InsuranceCompany, InvestmentFund)
            
            if success:
                print("\n✅ Database seeded successfully!")
                return True
            else:
                print("\n⚠️  Database seeding had issues")
                return False
        
    except Exception as e:
        print(f"\n❌ Error seeding database: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_database():
    """Verify database setup"""
    try:
        print("\n" + "="*70)
        print("🔍 STEP 4: Verification")
        print("="*70)
        
        from app import app, db
        from database.models import User, Budget, Expense, Income, ChatHistory
        from database.models import Bank, InsuranceCompany, InvestmentFund
        from sqlalchemy import inspect
        
        with app.app_context():
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"\n📊 Database Statistics:")
            print(f"   Total Tables: {len(tables)}")
            
            # Count records
            counts = {
                'Banks': Bank.query.count(),
                'Insurance Companies': InsuranceCompany.query.count(),
                'Investment Funds': InvestmentFund.query.count(),
                'Users': User.query.count(),
                'Budgets': Budget.query.count(),
                'Expenses': Expense.query.count(),
                'Incomes': Income.query.count(),
                'Chat History': ChatHistory.query.count()
            }
            
            print(f"\n📈 Record Counts:")
            for name, count in counts.items():
                status = "✅" if count > 0 or name in ['Users', 'Budgets', 'Expenses', 'Incomes', 'Chat History'] else "⚠️ "
                print(f"   {status} {name:<25} {count:>5} records")
            
            # Sample data check
            print(f"\n🏦 Sample Banks:")
            banks = Bank.query.limit(3).all()
            for bank in banks:
                print(f"   • {bank.name}")
                print(f"     Home Loan: {bank.home_loan_rate}% | Personal: {bank.personal_loan_rate}%")
            
            print(f"\n🛡️  Sample Insurance:")
            insurance = InsuranceCompany.query.limit(3).all()
            for ins in insurance:
                print(f"   • {ins.name}")
                print(f"     CSR: {ins.claim_settlement_ratio}% | Rating: {ins.rating}/5")
            
            print(f"\n📈 Sample Funds:")
            funds = InvestmentFund.query.limit(3).all()
            for fund in funds:
                print(f"   • {fund.fund_name}")
                print(f"     1Y: {fund.returns_1yr}% | 3Y: {fund.returns_3yr}% | 5Y: {fund.returns_5yr}%")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Verification error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main execution"""
    print("\n" + "="*70)
    print("🚀 CREDNEST AI - COMPLETE DATABASE RESET")
    print("="*70)
    print("\n⚠️  WARNING: This will delete all existing data!")
    print("   - All users will be removed")
    print("   - All budgets, expenses, incomes will be deleted")
    print("   - All chat history will be cleared")
    print("   - Database will be recreated from scratch")
    
    # Step 1: Drop and create database
    if not drop_and_create_database():
        print("\n❌ Failed at Step 1: Database Reset")
        sys.exit(1)
    
    # Step 2: Initialize tables
    if not initialize_tables():
        print("\n❌ Failed at Step 2: Table Initialization")
        sys.exit(1)
    
    # Step 3: Seed database
    if not seed_database():
        print("\n❌ Failed at Step 3: Database Seeding")
        sys.exit(1)
    
    # Step 4: Verify
    if not verify_database():
        print("\n❌ Failed at Step 4: Verification")
        sys.exit(1)
    
    # Success!
    print("\n" + "="*70)
    print("✅ DATABASE RESET COMPLETED SUCCESSFULLY!")
    print("="*70)
    print("\n🎉 Your CredNest AI database is ready!")
    print("\n📝 Next Steps:")
    print("   1. Start the application: python app.py")
    print("   2. Access at: http://localhost:5000")
    print("   3. Register a new user account")
    print("   4. Explore the financial data")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
