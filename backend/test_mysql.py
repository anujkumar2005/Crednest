"""Test MySQL connection"""
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

print("Testing MySQL connection...")
print(f"Host: {os.getenv('DB_HOST', '127.0.0.1')}")
print(f"Port: {os.getenv('DB_PORT', 3306)}")
print(f"User: {os.getenv('DB_USER', 'root')}")
print(f"Password: {'(empty)' if not os.getenv('DB_PASSWORD') else '(set)'}")

try:
    connection = pymysql.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        port=int(os.getenv('DB_PORT', 3306)),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        charset='utf8mb4'
    )
    print("\n✓ Connection successful!")
    
    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print(f"✓ MySQL version: {version[0]}")
    
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print(f"\n✓ Databases:")
    for db in databases:
        print(f"  - {db[0]}")
    
    cursor.close()
    connection.close()
    
except pymysql.Error as e:
    print(f"\n✗ Connection failed!")
    print(f"Error code: {e.args[0]}")
    print(f"Error message: {e.args[1]}")
    
    if e.args[0] == 1045:
        print("\n💡 This is an authentication error. Possible solutions:")
        print("   1. Check if your MySQL root password is correct")
        print("   2. Try connecting with MySQL Workbench to verify credentials")
        print("   3. Update DB_PASSWORD in .env file if password is required")
    elif e.args[0] == 2003:
        print("\n💡 Cannot connect to MySQL server. Check if:")
        print("   1. MySQL service is running")
        print("   2. Port 3306 is not blocked by firewall")
        print("   3. MySQL is configured to accept connections on 127.0.0.1")
