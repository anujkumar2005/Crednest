"""Test MySQL passwords"""
import pymysql

passwords = ["Anuj@2005", "1984"]

for pwd in passwords:
    print(f"\nTesting password: {pwd}")
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password=pwd,
            charset='utf8mb4'
        )
        print(f"✓ SUCCESS! Password '{pwd}' works!")
        
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✓ MySQL version: {version[0]}")
        
        cursor.close()
        connection.close()
        
        # Save the working password
        with open('working_password.txt', 'w') as f:
            f.write(pwd)
        
        break
        
    except pymysql.Error as e:
        print(f"✗ Failed: {e.args[1]}")
