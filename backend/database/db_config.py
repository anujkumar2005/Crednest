# MySQL Database Configuration Helper
# Run this first to set up the database

import os
from dotenv import load_dotenv

load_dotenv()

def get_database_uri():
    """Generate database URI based on configuration"""
    db_type = os.getenv('DB_TYPE', 'sqlite')
    
    if db_type == 'mysql':
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '3306')
        db_name = os.getenv('DB_NAME', 'crednest_db')
        db_user = os.getenv('DB_USER', 'root')
        db_password = os.getenv('DB_PASSWORD', '')
        db_charset = os.getenv('DB_CHARSET', 'utf8mb4')
        
        # MySQL connection string
        if db_password:
            uri = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset={db_charset}"
        else:
            uri = f"mysql+pymysql://{db_user}@{db_host}:{db_port}/{db_name}?charset={db_charset}"
        
        return uri
    else:
        # SQLite fallback
        return 'sqlite:///crednest.db'


def create_mysql_database():
    """Create MySQL database if it doesn't exist"""
    import pymysql
    
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = int(os.getenv('DB_PORT', '3306'))
    db_name = os.getenv('DB_NAME', 'crednest_db')
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', '')
    
    try:
        # Connect to MySQL server (without database)
        connection = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password
        )
        
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print(f"✓ Database '{db_name}' created/verified successfully")
        
        cursor.close()
        connection.close()
        return True
        
    except Exception as e:
        print(f"✗ Error creating database: {e}")
        print("\n💡 Make sure MySQL is running and credentials are correct in .env file")
        return False


if __name__ == '__main__':
    print("="*70)
    print("🗄️  CredNest AI - Database Setup")
    print("="*70)
    
    db_type = os.getenv('DB_TYPE', 'sqlite')
    print(f"\nDatabase Type: {db_type.upper()}")
    
    if db_type == 'mysql':
        print("\nCreating MySQL database...")
        if create_mysql_database():
            print(f"\n✓ Database URI: {get_database_uri()}")
            print("\n✓ Ready to run app.py")
        else:
            print("\n✗ Database setup failed")
            print("\nTroubleshooting:")
            print("1. Make sure MySQL is installed and running")
            print("2. Check DB_USER and DB_PASSWORD in .env file")
            print("3. Verify MySQL is accessible on the configured host/port")
    else:
        print(f"\n✓ Using SQLite database")
        print(f"✓ Database URI: {get_database_uri()}")
    
    print("="*70)
