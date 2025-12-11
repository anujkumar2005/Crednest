"""
Initialize MySQL Database for CredNest AI
Creates the database if it doesn't exist and sets up all tables
"""

import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_database():
    """Create the MySQL database if it doesn't exist"""
    try:
        # Connect to MySQL server (without specifying database)
        connection = pymysql.connect(
            host=os.getenv('DB_HOST', '127.0.0.1'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        db_name = os.getenv('DB_NAME', 'crednest_db')
        
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print(f"✓ Database '{db_name}' created or already exists")
        
        # Show databases
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print(f"\n📊 Available databases:")
        for db in databases:
            print(f"   - {db[0]}")
        
        cursor.close()
        connection.close()
        
        return True
        
    except pymysql.Error as e:
        print(f"✗ MySQL Error: {e}")
        print(f"\n💡 Make sure MySQL server is running on {os.getenv('DB_HOST', '127.0.0.1')}:{os.getenv('DB_PORT', 3306)}")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def initialize_tables():
    """Initialize database tables using Flask-SQLAlchemy"""
    try:
        from app import app, db
        
        with app.app_context():
            # Create all tables
            db.create_all()
            print("\n✓ Database tables created successfully!")
            
            # Show created tables
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"\n📋 Created tables ({len(tables)}):")
            for table in tables:
                print(f"   - {table}")
            
        return True
        
    except Exception as e:
        print(f"✗ Error creating tables: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🗄️  CredNest AI - MySQL Database Initialization")
    print("=" * 60)
    
    # Step 1: Create database
    print("\n[Step 1] Creating database...")
    if not create_database():
        print("\n⚠️  Failed to create database. Please check your MySQL configuration.")
        exit(1)
    
    # Step 2: Initialize tables
    print("\n[Step 2] Initializing database tables...")
    if not initialize_tables():
        print("\n⚠️  Failed to create tables. Please check the error above.")
        exit(1)
    
    print("\n" + "=" * 60)
    print("✅ Database initialization complete!")
    print("=" * 60)
    print("\n💡 You can now start the Flask application with: python app.py")
