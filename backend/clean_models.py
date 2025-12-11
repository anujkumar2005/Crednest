"""
Clean null bytes from models.py file
"""

import os

# Read the file in binary mode
with open('database/models.py', 'rb') as f:
    content = f.read()

print(f"Original file size: {len(content)} bytes")
print(f"Null bytes found: {content.count(b'\\x00')}")

# Remove null bytes
cleaned = content.replace(b'\x00', b'')

print(f"Cleaned file size: {len(cleaned)} bytes")
print(f"Removed {len(content) - len(cleaned)} null bytes")

# Write cleaned content back
with open('database/models.py', 'wb') as f:
    f.write(cleaned)

print("✅ File cleaned successfully!")
