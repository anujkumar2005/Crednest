"""
CredNest AI - Database Models
Complete schema for ultra-premium financial platform
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


def format_timestamp(dt):
    """Format datetime to ISO string"""
    if dt:
        return dt.isoformat()
    return None


class User(UserMixin, db.Model):
    """Enhanced User model with comprehensive profile"""
    __tablename__ = 'users'
    
    # Authentication
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Basic Info
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))  # Male, Female, Other, Prefer not to say
    date_of_birth = db.Column(db.Date)
    phone = db.Column(db.String(20))
    
    # Address
    address = db.Column(db.Text)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100), default='India')
    pincode = db.Column(db.String(10))
    
    # Professional
    occupation = db.Column(db.String(100))
    company = db.Column(db.String(150))
    monthly_income = db.Column(db.Float)
    
    # Profile
    profile_image = db.Column(db.String(255))
    bio = db.Column(db.Text)
    profile_completed = db.Column(db.Boolean, default=False)
    
    # Account Status
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    last_login = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    chat_history = db.relationship('ChatHistory', backref='user', lazy=True, cascade='all, delete-orphan')
    budgets = db.relationship('Budget', backref='user', lazy=True, cascade='all, delete-orphan')
    expenses = db.relationship('Expense', backref='user', lazy=True, cascade='all, delete-orphan')
    incomes = db.relationship('Income', backref='user', lazy=True, cascade='all, delete-orphan')
    feedback = db.relationship('Feedback', backref='user', lazy=True, cascade='all, delete-orphan')
    
    # Extra relationships (kept for compatibility)
    savings_goals = db.relationship('SavingsGoal', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    investments = db.relationship('Investment', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    loans = db.relationship('Loan', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    insurance_policies = db.relationship('InsurancePolicy', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'pincode': self.pincode,
            'occupation': self.occupation,
            'company': self.company,
            'monthly_income': self.monthly_income,
            'profile_image': self.profile_image,
            'bio': self.bio,
            'profile_completed': self.profile_completed,
            'is_verified': self.is_verified,
            'created_at': format_timestamp(self.created_at),
            'last_login': format_timestamp(self.last_login),
            'updated_at': format_timestamp(self.updated_at)
        }
    
    def __repr__(self):
        return f'<User {self.email}>'


class ChatHistory(db.Model):
    """AI chat conversation history"""
    __tablename__ = 'chat_history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_id = db.Column(db.String(100), nullable=False, index=True)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    tool_used = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'session_id': self.session_id,
            'message': self.message,
            'response': self.response,
            'tool_used': self.tool_used,
            'created_at': format_timestamp(self.created_at)
        }


class Budget(db.Model):
    """Budget categories and limits"""
    __tablename__ = 'budgets'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    period = db.Column(db.String(20), default='monthly')
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'amount': self.amount,
            'period': self.period,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None
        }


class Expense(db.Model):
    """Expense tracking"""
    __tablename__ = 'expenses'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    payment_method = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'amount': self.amount,
            'description': self.description,
            'date': self.date.isoformat(),
            'payment_method': self.payment_method
        }


class Income(db.Model):
    """Income tracking"""
    __tablename__ = 'incomes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    recurring = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'source': self.source,
            'amount': self.amount,
            'description': self.description,
            'date': self.date.isoformat(),
            'recurring': self.recurring
        }


class Feedback(db.Model):
    """User feedback and suggestions"""
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')
    admin_response = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category': self.category,
            'rating': self.rating,
            'subject': self.subject,
            'message': self.message,
            'status': self.status,
            'admin_response': self.admin_response,
            'created_at': format_timestamp(self.created_at),
            'updated_at': format_timestamp(self.updated_at)
        }


class Bank(db.Model):
    """Bank information and loan rates"""
    __tablename__ = 'banks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    logo_url = db.Column(db.String(500))
    home_loan_rate = db.Column(db.Float)
    personal_loan_rate = db.Column(db.Float)
    car_loan_rate = db.Column(db.Float)
    education_loan_rate = db.Column(db.Float)
    processing_fee = db.Column(db.Float)
    min_cibil_score = db.Column(db.Integer)
    max_loan_amount = db.Column(db.Float)
    min_loan_amount = db.Column(db.Float)
    max_tenure_years = db.Column(db.Integer)
    description = db.Column(db.Text)
    website = db.Column(db.String(200))
    customer_care = db.Column(db.String(50))
    rating = db.Column(db.Float)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo_url': self.logo_url,
            'home_loan_rate': self.home_loan_rate,
            'personal_loan_rate': self.personal_loan_rate,
            'car_loan_rate': self.car_loan_rate,
            'education_loan_rate': self.education_loan_rate,
            'processing_fee': self.processing_fee,
            'min_cibil_score': self.min_cibil_score,
            'max_loan_amount': self.max_loan_amount,
            'min_loan_amount': self.min_loan_amount,
            'max_tenure_years': self.max_tenure_years,
            'description': self.description,
            'website': self.website,
            'customer_care': self.customer_care,
            'rating': self.rating
        }


class InsuranceCompany(db.Model):
    """Insurance company information"""
    __tablename__ = 'insurance_companies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    logo_url = db.Column(db.String(500))
    claim_settlement_ratio = db.Column(db.Float)
    life_insurance_premium = db.Column(db.Float)
    health_insurance_premium = db.Column(db.Float)
    vehicle_insurance_premium = db.Column(db.Float)
    coverage_amount = db.Column(db.Float)
    rating = db.Column(db.Float)
    description = db.Column(db.Text)
    website = db.Column(db.String(200))
    customer_care = db.Column(db.String(50))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo_url': self.logo_url,
            'claim_settlement_ratio': self.claim_settlement_ratio,
            'life_insurance_premium': self.life_insurance_premium,
            'health_insurance_premium': self.health_insurance_premium,
            'vehicle_insurance_premium': self.vehicle_insurance_premium,
            'coverage_amount': self.coverage_amount,
            'rating': self.rating,
            'description': self.description,
            'website': self.website,
            'customer_care': self.customer_care
        }


class InvestmentFund(db.Model):
    """Investment fund information"""
    __tablename__ = 'investment_funds'
    
    id = db.Column(db.Integer, primary_key=True)
    fund_name = db.Column(db.String(200), nullable=False)
    fund_type = db.Column(db.String(50), nullable=False)
    amc_name = db.Column(db.String(100))
    nav = db.Column(db.Float, nullable=False)
    returns_1yr = db.Column(db.Float)
    returns_3yr = db.Column(db.Float)
    returns_5yr = db.Column(db.Float)
    expense_ratio = db.Column(db.Float)
    min_investment = db.Column(db.Float)
    min_sip = db.Column(db.Float)
    risk_level = db.Column(db.String(20))
    rating = db.Column(db.Float)
    description = db.Column(db.Text)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'fund_name': self.fund_name,
            'fund_type': self.fund_type,
            'amc_name': self.amc_name,
            'nav': self.nav,
            'returns': {
                '1yr': self.returns_1yr,
                '3yr': self.returns_3yr,
                '5yr': self.returns_5yr
            },
            'expense_ratio': self.expense_ratio,
            'min_investment': self.min_investment,
            'min_sip': self.min_sip,
            'risk_level': self.risk_level,
            'rating': self.rating,
            'description': self.description
        }


# Additional models for compatibility
class SavingsGoal(db.Model):
    """Savings goals tracking"""
    __tablename__ = 'savings_goals'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    goal_name = db.Column(db.String(100), nullable=False)
    target_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0)
    target_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Investment(db.Model):
    """Investment tracking"""
    __tablename__ = 'investments'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    investment_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    current_value = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Loan(db.Model):
    """Loan tracking"""
    __tablename__ = 'loans'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    loan_type = db.Column(db.String(50), nullable=False)
    bank_name = db.Column(db.String(100))
    loan_amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float)
    tenure_months = db.Column(db.Integer)
    emi = db.Column(db.Float)
    start_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class InsurancePolicy(db.Model):
    """Insurance policy tracking"""
    __tablename__ = 'insurance_policies'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    policy_type = db.Column(db.String(50), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    policy_number = db.Column(db.String(100), unique=True)
    premium_amount = db.Column(db.Float, nullable=False)
    coverage_amount = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
