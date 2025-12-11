# Quick Start Script for CredNest AI
# This script runs the application with simplified database setup

import os
import sys

print("\n" + "="*70)
print("🏦  CredNest AI - Starting Application")
print("="*70)

# Change to backend directory
os.chdir(os.path.dirname(__file__))

# Run the Flask app
print("\n✓ Starting Flask server...")
print("📍 Navigate to: http://localhost:5000")
print("="*70 + "\n")

os.system("python app.py")
