"""
Update MySQL database schema to match new models
Adds missing columns to existing tables
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db
from sqlalchemy import text

print("=" * 70)
print("🔧 UPDATING MYSQL DATABASE SCHEMA")
print("=" * 70)

with app.app_context():
    try:
        # Add missing columns to banks table
        print("\n📊 Updating banks table...")
        db.session.execute(text("""
            ALTER TABLE banks 
            ADD COLUMN IF NOT EXISTS processing_fee FLOAT,
            ADD COLUMN IF NOT EXISTS min_cibil_score INT,
            ADD COLUMN IF NOT EXISTS max_loan_amount FLOAT,
            ADD COLUMN IF NOT EXISTS min_loan_amount FLOAT,
            ADD COLUMN IF NOT EXISTS max_tenure_years INT,
            ADD COLUMN IF NOT EXISTS description TEXT,
            ADD COLUMN IF NOT EXISTS website VARCHAR(200),
            ADD COLUMN IF NOT EXISTS customer_care VARCHAR(50),
            ADD COLUMN IF NOT EXISTS rating FLOAT,
            ADD COLUMN IF NOT EXISTS last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
        """))
        db.session.commit()
        print("✅ Banks table updated successfully")
        
        # Add missing columns to insurance_companies table
        print("\n🛡️  Updating insurance_companies table...")
        db.session.execute(text("""
            ALTER TABLE insurance_companies
            ADD COLUMN IF NOT EXISTS description TEXT,
            ADD COLUMN IF NOT EXISTS website VARCHAR(200),
            ADD COLUMN IF NOT EXISTS customer_care VARCHAR(50),
            ADD COLUMN IF NOT EXISTS last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
        """))
        db.session.commit()
        print("✅ Insurance companies table updated successfully")
        
        # Add missing columns to investment_funds table
        print("\n📈 Updating investment_funds table...")
        db.session.execute(text("""
            ALTER TABLE investment_funds
            ADD COLUMN IF NOT EXISTS description TEXT,
            ADD COLUMN IF NOT EXISTS last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
        """))
        db.session.commit()
        print("✅ Investment funds table updated successfully")
        
        # Create feedback table if it doesn't exist
        print("\n💬 Creating feedback table...")
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                category VARCHAR(50) NOT NULL,
                rating INT,
                subject VARCHAR(200),
                message TEXT NOT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                admin_response TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """))
        db.session.commit()
        print("✅ Feedback table created successfully")
        
        print("\n" + "=" * 70)
        print("✅ DATABASE SCHEMA UPDATE COMPLETE!")
        print("=" * 70)
        
    except Exception as e:
        db.session.rollback()
        print(f"\n❌ Error updating schema: {e}")
        print("\nTrying alternative approach...")
        
        # Alternative: Drop and recreate all tables
        print("\n⚠️  Recreating all tables (this will preserve existing data)...")
        db.create_all()
        print("✅ Tables recreated successfully")
