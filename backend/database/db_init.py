"""
CredNest AI - Database Initialization
Initialize database and seed with sample data
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask
from database.models import db
from database.seed_data import seed_all_data

def init_database(app):
    """Initialize database with all tables"""
    with app.app_context():
        print("\n" + "="*70)
        print("🗄️   Initializing CredNest AI Database")
        print("="*70)
        
        try:
            # Create all tables
            db.create_all()
            print("✓ Database tables created successfully")
            
            # Check if data already exists
            from database.models import Bank, InsuranceCompany, InvestmentFund
            
            if Bank.query.count() == 0:
                print("\n📝  No existing data found. Seeding database...")
                seed_all_data()
            else:
                print(f"\n✓ Database already contains data:")
                print(f"   → Banks: {Bank.query.count()}")
                print(f"   → Insurance Companies: {InsuranceCompany.query.count()}")
                print(f"   → Investment Funds: {InvestmentFund.query.count()}")
                print("\n💡  To reseed, delete the database file and restart.")
            
            print("="*70 + "\n")
            return True
            
        except Exception as e:
            print(f"\n❌  Database initialization failed: {e}\n")
            return False


def reset_database(app):
    """Reset database - WARNING: Deletes all data!"""
    with app.app_context():
        print("\n" + "="*70)
        print("⚠️   RESETTING DATABASE - ALL DATA WILL BE LOST!")
        print("="*70)
        
        try:
            db.drop_all()
            print("✓ All tables dropped")
            
            db.create_all()
            print("✓ Tables recreated")
            
            seed_all_data()
            
            print("="*70)
            print("✅  Database reset completed!")
            print("="*70 + "\n")
            return True
            
        except Exception as e:
            print(f"\n❌  Database reset failed: {e}\n")
            return False


if __name__ == '__main__':
    # Create minimal Flask app for database operations
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crednest.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--reset':
        reset_database(app)
    else:
        init_database(app)
