"""
Add Feedback model to database
Run this to create the feedback table
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db

# Define Feedback model inline
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime

class Feedback(db.Model):
    """User feedback and suggestions"""
    __tablename__ = 'feedback'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category = Column(String(50), nullable=False)
    rating = Column(Integer)
    subject = Column(String(200))
    message = Column(Text, nullable=False)
    status = Column(String(20), default='pending')
    admin_response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

print("Creating Feedback table...")
with app.app_context():
    db.create_all()
    print("✅ Feedback table created successfully!")
