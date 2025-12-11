"""
CredNest AI - Enhanced Backend Application
Complete financial platform with improved chat history and AI response management
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
import os
import logging
import sys
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# CONFIGURATION
# ============================================================================

class Config:
    """Application configuration"""
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'crednest-ultra-secret-2025')
    PERMANENT_SESSION_LIFETIME = 604800  # 7 days
    
    # Database - MySQL Support
    @staticmethod
    def get_database_uri():
        """Generate database URI based on DB_TYPE in .env"""
        db_type = os.getenv('DB_TYPE', 'sqlite')
        
        if db_type == 'mysql':
            db_host = os.getenv('DB_HOST', 'localhost')
            db_port = os.getenv('DB_PORT', '3306')
            db_name = os.getenv('DB_NAME', 'crednest_db')
            db_user = os.getenv('DB_USER', 'root')
            db_password = os.getenv('DB_PASSWORD', '')
            db_charset = os.getenv('DB_CHARSET', 'utf8mb4')
            
            if db_password:
                return f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset={db_charset}"
            else:
                return f"mysql+pymysql://{db_user}@{db_host}:{db_port}/{db_name}?charset={db_charset}"
        else:
            return 'sqlite:///crednest.db'
    
    SQLALCHEMY_DATABASE_URI = get_database_uri.__func__()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }
    
    # AI Settings
    GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'your-groq-api-key-here')
    AI_MODEL = 'llama-3.3-70b-versatile'
    
    # Chat Settings
    ENABLE_TYPING_DELAY = os.getenv('ENABLE_TYPING_DELAY', 'true').lower() == 'true'
    TYPING_DELAY_MIN = float(os.getenv('TYPING_DELAY_MIN', '0.5'))
    TYPING_DELAY_MAX = float(os.getenv('TYPING_DELAY_MAX', '3.0'))
    TYPING_WPM = int(os.getenv('TYPING_WPM', '200'))
    MAX_MESSAGE_LENGTH = 2000
    DEFAULT_HISTORY_LIMIT = 8
    MAX_HISTORY_LIMIT = 50
    
    # Pagination
    DEFAULT_PAGE_SIZE = 20
    MAX_PAGE_SIZE = 100



# ============================================================================
# APPLICATION INITIALIZATION
# ============================================================================

app = Flask(__name__, 
    template_folder='../frontend',
    static_folder='../frontend',
    static_url_path='')

app.config.from_object(Config)

# Initialize extensions
# Initialize extensions
from database.models import db, User, ChatHistory, Budget, Expense, Income, Bank, InsuranceCompany, InvestmentFund
db.init_app(app)
CORS(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index'
login_manager.login_message = 'Please log in to access this page'

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import utilities
from utils import (
    calculate_typing_delay,
    simulate_typing_delay,
    paginate_query,
    sanitize_user_input,
    format_chat_session,
    get_session_title,
    format_timestamp,
    calculate_response_time,
    validate_session_id,
    truncate_history
)

# ============================================================================
# DATABASE MODELS
# ============================================================================

# Models are now imported from database.models



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ============================================================================
# AI INITIALIZATION
# ============================================================================

conversation_manager = None

def init_finance_ai():
    """Initialize Finance Expert AI with error handling"""
    global conversation_manager
    try:
        sys.path.insert(0, os.path.dirname(__file__))
        from ai.conversation_manager import ConversationManager
        
        api_key = Config.GROQ_API_KEY
        
        if not api_key or api_key == 'your-groq-api-key-here':
            logger.warning("⚠️  No valid Groq API key found - AI will be disabled")
            return False
        
        conversation_manager = ConversationManager(api_key)
        logger.info("✓ Finance Expert AI initialized successfully")
        return True
        
    except ImportError as e:
        logger.error(f"✗ Failed to import AI modules: {e}")
        logger.info("💡 Make sure ai/ and tools/ folders exist with all required files")
        return False
    except Exception as e:
        logger.error(f"✗ AI initialization failed: {e}")
        return False

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_session_metadata(session_id: str, user_id: int) -> dict:
    """Get metadata for a chat session"""
    try:
        # Get first and last messages
        first_msg = ChatHistory.query.filter_by(
            session_id=session_id,
            user_id=user_id
        ).order_by(ChatHistory.created_at.asc()).first()
        
        last_msg = ChatHistory.query.filter_by(
            session_id=session_id,
            user_id=user_id
        ).order_by(ChatHistory.created_at.desc()).first()
        
        # Get message count
        count = ChatHistory.query.filter_by(
            session_id=session_id,
            user_id=user_id
        ).count()
        
        if not first_msg:
            return None
        
        return {
            'session_id': session_id,
            'title': get_session_title(first_msg.message),
            'message_count': count,
            'created_at': format_timestamp(first_msg.created_at),
            'last_message_at': format_timestamp(last_msg.created_at) if last_msg else None,
            'preview': first_msg.message[:100]
        }
    except Exception as e:
        logger.error(f"Error getting session metadata: {e}")
        return None


def get_conversation_context(session_id: str, user_id: int, limit: int = 8) -> list:
    """Get conversation context for AI"""
    try:
        chats = ChatHistory.query.filter_by(
            session_id=session_id,
            user_id=user_id
        ).order_by(ChatHistory.created_at.desc()).limit(limit).all()
        
        # Reverse to chronological order
        chats = list(reversed(chats))
        
        context = []
        for chat in chats:
            context.append({
                'user': chat.message,
                'assistant': chat.response,
                'timestamp': chat.created_at
            })
        
        return context
    except Exception as e:
        logger.error(f"Error getting conversation context: {e}")
        return []

# ============================================================================
# FRONTEND ROUTES
# ============================================================================

@app.route('/')
def index():
    """Landing page / Login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('1-login.html')

@app.route('/login')
def login_page():
    """Login page"""
    return redirect(url_for('index'))

@app.route('/about')
def about():
    """About page"""
    return render_template('2-about.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard"""
    return render_template('3-dashboard.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('17-contact.html')

# ============================================================================
# MODULE ROUTES
# ============================================================================

@app.route('/budgeting')
@login_required
def budgeting():
    """Budgeting module"""
    return render_template('modules/4-budgeting.html')

@app.route('/savings')
@login_required
def savings():
    """Savings module"""
    return render_template('modules/5-savings.html')

@app.route('/investments')
@login_required
def investments():
    """Investments module"""
    return render_template('modules/6-investments.html')

@app.route('/loans')
@login_required
def loans():
    """Loans module"""
    return render_template('modules/7-loans.html')

@app.route('/insurance')
@login_required
def insurance():
    """Insurance module"""
    return render_template('modules/8-insurance.html')

@app.route('/chat')
@login_required
def chat():
    """AI Chat module"""
    return render_template('modules/9-chat.html')

# ============================================================================
# USER PAGES
# ============================================================================

@app.route('/profile')
@login_required
def profile():
    """User profile page"""
    return render_template('user/14-profile.html')

@app.route('/chat-history')
@login_required
def chat_history_page():
    """Chat history page"""
    return render_template('user/15-chat-history.html')

@app.route('/expense-tracker')
@login_required
def expense_tracker():
    """Expense tracking page"""
    return render_template('user/16-expense-tracker.html')

# ============================================================================
# DETAIL PAGES
# ============================================================================

@app.route('/bank-details/<int:bank_id>')
@login_required
def bank_details(bank_id):
    """Bank details page"""
    return render_template('details/10-bank-details.html')

@app.route('/insurance-details/<int:company_id>')
@login_required
def insurance_details(company_id):
    """Insurance company details page"""
    return render_template('details/11-insurance-details.html')

@app.route('/investment-details/<int:fund_id>')
@login_required
def investment_details(fund_id):
    """Investment fund details page"""
    return render_template('details/12-investment-details.html')

@app.route('/loan-details/<int:loan_id>')
@login_required
def loan_details(loan_id):
    """Loan details page"""
    return render_template('details/13-loan-details.html')

# ============================================================================
# API ROUTES - AUTHENTICATION
# ============================================================================

@app.route('/api/auth/register', methods=['POST'])
def api_register():
    """User registration API"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        email = data.get('email', '').strip().lower()
        password = data.get('password', '').strip()
        name = data.get('name', '').strip()
        
        # Validation
        if not all([email, password, name]):
            return jsonify({'error': 'All fields are required'}), 400
        
        if len(password) < 6:
            return jsonify({'error': 'Password must be at least 6 characters'}), 400
        
        # Check if user exists
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already registered'}), 400
        
        # Create user
        user = User(email=email, name=name)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        # Auto login
        login_user(user, remember=True)
        
        logger.info(f"✓ New user registered: {email}")
        
        return jsonify({
            'message': 'Registration successful',
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Registration error: {e}")
        return jsonify({'error': 'Registration failed. Please try again.'}), 500

@app.route('/api/auth/login', methods=['POST'])
def api_login():
    """User login API"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        email = data.get('email', '').strip().lower()
        password = data.get('password', '').strip()
        
        if not all([email, password]):
            return jsonify({'error': 'Email and password required'}), 400
        
        # Find user
        user = User.query.filter_by(email=email).first()
        
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid email or password'}), 401
        
        # Update last login
        user.last_login = datetime.utcnow()
        db.session.commit()
        
        # Login user
        login_user(user, remember=True)
        
        logger.info(f"✓ User logged in: {email}")
        
        return jsonify({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email
            }
        }), 200
        
    except Exception as e:
        logger.error(f"Login error: {e}")
        return jsonify({'error': 'Login failed. Please try again.'}), 500

@app.route('/api/auth/logout', methods=['POST'])
@login_required
def api_logout():
    """User logout API"""
    try:
        user_email = current_user.email
        logout_user()
        logger.info(f"✓ User logged out: {user_email}")
        return jsonify({'message': 'Logged out successfully'}), 200
    except Exception as e:
        logger.error(f"Logout error: {e}")
        return jsonify({'error': 'Logout failed'}), 500

@app.route('/api/auth/profile', methods=['GET'])
@login_required
def api_profile():
    """Get user profile"""
    try:
        return jsonify({
            'id': current_user.id,
            'name': current_user.name,
            'email': current_user.email,
            'created_at': format_timestamp(current_user.created_at),
            'last_login': format_timestamp(current_user.last_login)
        }), 200
    except Exception as e:
        logger.error(f"Profile error: {e}")
        return jsonify({'error': 'Failed to load profile'}), 500

@app.route('/api/profile/update', methods=['PUT'])
@login_required
def api_update_profile():
    """Update user profile"""
    try:
        data = request.get_json()
        
        # Update basic info
        if 'name' in data:
            current_user.name = data['name']
        if 'age' in data:
            current_user.age = data['age']
        if 'gender' in data:
            current_user.gender = data['gender']
        if 'date_of_birth' in data:
            current_user.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        if 'phone' in data:
            current_user.phone = data['phone']
        
        # Update address
        if 'address' in data:
            current_user.address = data['address']
        if 'city' in data:
            current_user.city = data['city']
        if 'state' in data:
            current_user.state = data['state']
        if 'pincode' in data:
            current_user.pincode = data['pincode']
        
        # Update professional
        if 'occupation' in data:
            current_user.occupation = data['occupation']
        if 'company' in data:
            current_user.company = data['company']
        if 'monthly_income' in data:
            current_user.monthly_income = float(data['monthly_income'])
        
        # Update profile
        if 'bio' in data:
            current_user.bio = data['bio']
        
        # Check if profile is completed
        required_fields = [current_user.name, current_user.phone, current_user.city]
        current_user.profile_completed = all(required_fields)
        
        db.session.commit()
        
        logger.info(f"✓ Profile updated for user {current_user.email}")
        
        return jsonify({
            'message': 'Profile updated successfully',
            'profile': current_user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Profile update error: {e}")
        return jsonify({'error': 'Failed to update profile'}), 500

# ============================================================================
# API ROUTES - BUDGET MANAGEMENT
# ============================================================================

@app.route('/api/budgets/create', methods=['POST'])
@login_required
def api_create_budget():
    """Create monthly budget with categories"""
    try:
        data = request.get_json()
        
        month = data.get('month')  # Format: YYYY-MM
        categories = data.get('categories', [])
        
        if not month or not categories:
            return jsonify({'error': 'Month and categories required'}), 400
        
        created_budgets = []
        
        for cat in categories:
            budget = Budget(
                user_id=current_user.id,
                month=month,
                category=cat.get('category'),
                planned_amount=float(cat.get('planned_amount', 0)),
                icon=cat.get('icon', '📦'),
                color=cat.get('color', '#95A5A6'),
                notes=cat.get('notes', '')
            )
            db.session.add(budget)
            created_budgets.append(budget)
        
        db.session.commit()
        
        logger.info(f"✓ Created {len(created_budgets)} budgets for {current_user.email}")
        
        return jsonify({
            'message': 'Budgets created successfully',
            'budgets': [b.to_dict() for b in created_budgets]
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Budget creation error: {e}")
        return jsonify({'error': 'Failed to create budgets'}), 500

@app.route('/api/budgets/month/<month>', methods=['GET'])
@login_required
def api_get_monthly_budget(month):
    """Get budget for a specific month"""
    try:
        budgets = Budget.query.filter_by(
            user_id=current_user.id,
            month=month,
            is_active=True
        ).all()
        
        # Get total income for the month
        incomes = Income.query.filter_by(
            user_id=current_user.id,
            month=month
        ).all()
        
        total_income = sum(inc.amount for inc in incomes)
        total_planned = sum(b.planned_amount for b in budgets)
        total_spent = sum(b.spent_amount for b in budgets)
        
        return jsonify({
            'month': month,
            'total_income': total_income,
            'total_planned': total_planned,
            'total_spent': total_spent,
            'remaining': total_income - total_spent,
            'savings': total_income - total_spent,
            'budgets': [b.to_dict() for b in budgets],
            'incomes': [inc.to_dict() for inc in incomes]
        }), 200
        
    except Exception as e:
        logger.error(f"Monthly budget error: {e}")
        return jsonify({'error': 'Failed to load budget'}), 500

@app.route('/api/budgets/<int:budget_id>', methods=['PUT'])
@login_required
def api_update_budget(budget_id):
    """Update budget category"""
    try:
        budget = Budget.query.filter_by(
            id=budget_id,
            user_id=current_user.id
        ).first()
        
        if not budget:
            return jsonify({'error': 'Budget not found'}), 404
        
        data = request.get_json()
        
        if 'planned_amount' in data:
            budget.planned_amount = float(data['planned_amount'])
        if 'icon' in data:
            budget.icon = data['icon']
        if 'color' in data:
            budget.color = data['color']
        if 'notes' in data:
            budget.notes = data['notes']
        if 'is_active' in data:
            budget.is_active = data['is_active']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Budget updated successfully',
            'budget': budget.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Budget update error: {e}")
        return jsonify({'error': 'Failed to update budget'}), 500

@app.route('/api/budgets/<int:budget_id>', methods=['DELETE'])
@login_required
def api_delete_budget(budget_id):
    """Delete budget category"""
    try:
        budget = Budget.query.filter_by(
            id=budget_id,
            user_id=current_user.id
        ).first()
        
        if not budget:
            return jsonify({'error': 'Budget not found'}), 404
        
        db.session.delete(budget)
        db.session.commit()
        
        return jsonify({'message': 'Budget deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Budget delete error: {e}")
        return jsonify({'error': 'Failed to delete budget'}), 500

# ============================================================================
# API ROUTES - EXPENSE MANAGEMENT
# ============================================================================

@app.route('/api/expenses/add', methods=['POST'])
@login_required
def api_add_expense():
    """Add new expense"""
    try:
        data = request.get_json()
        
        expense = Expense(
            user_id=current_user.id,
            amount=float(data.get('amount')),
            category=data.get('category'),
            description=data.get('description', ''),
            date=datetime.strptime(data.get('date'), '%Y-%m-%d').date() if data.get('date') else datetime.utcnow().date(),
            payment_method=data.get('payment_method'),
            location=data.get('location'),
            tags=data.get('tags', ''),
            notes=data.get('notes', ''),
            is_recurring=data.get('is_recurring', False),
            recurring_frequency=data.get('recurring_frequency')
        )
        
        db.session.add(expense)
        
        # Update budget spent amount
        month = expense.date.strftime('%Y-%m')
        budget = Budget.query.filter_by(
            user_id=current_user.id,
            month=month,
            category=expense.category
        ).first()
        
        if budget:
            budget.spent_amount += expense.amount
        
        db.session.commit()
        
        logger.info(f"✓ Expense added: ₹{expense.amount} - {expense.category}")
        
        return jsonify({
            'message': 'Expense added successfully',
            'expense': expense.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Expense add error: {e}")
        return jsonify({'error': 'Failed to add expense'}), 500

@app.route('/api/expenses', methods=['GET'])
@login_required
def api_get_expenses():
    """Get expenses with filters"""
    try:
        month = request.args.get('month')
        category = request.args.get('category')
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 50, type=int)
        
        query = Expense.query.filter_by(user_id=current_user.id)
        
        if month:
            start_date = datetime.strptime(f"{month}-01", '%Y-%m-%d').date()
            import calendar
            last_day = calendar.monthrange(start_date.year, start_date.month)[1]
            end_date = datetime.strptime(f"{month}-{last_day}", '%Y-%m-%d').date()
            query = query.filter(Expense.date >= start_date, Expense.date <= end_date)
        
        if category:
            query = query.filter_by(category=category)
        
        query = query.order_by(Expense.date.desc())
        
        result = paginate_query(query, page, limit)
        
        return jsonify({
            'expenses': [exp.to_dict() for exp in result['items']],
            'pagination': result['pagination']
        }), 200
        
    except Exception as e:
        logger.error(f"Expenses get error: {e}")
        return jsonify({'error': 'Failed to load expenses'}), 500

@app.route('/api/expenses/<int:expense_id>', methods=['PUT', 'DELETE'])
@login_required
def api_manage_expense(expense_id):
    """Update or delete expense"""
    try:
        expense = Expense.query.filter_by(
            id=expense_id,
            user_id=current_user.id
        ).first()
        
        if not expense:
            return jsonify({'error': 'Expense not found'}), 404
        
        if request.method == 'DELETE':
            # Update budget
            month = expense.date.strftime('%Y-%m')
            budget = Budget.query.filter_by(
                user_id=current_user.id,
                month=month,
                category=expense.category
            ).first()
            
            if budget:
                budget.spent_amount -= expense.amount
            
            db.session.delete(expense)
            db.session.commit()
            
            return jsonify({'message': 'Expense deleted successfully'}), 200
        
        else:  # PUT
            data = request.get_json()
            old_amount = expense.amount
            old_category = expense.category
            
            if 'amount' in data:
                expense.amount = float(data['amount'])
            if 'category' in data:
                expense.category = data['category']
            if 'description' in data:
                expense.description = data['description']
            if 'payment_method' in data:
                expense.payment_method = data['payment_method']
            if 'location' in data:
                expense.location = data['location']
            if 'tags' in data:
                expense.tags = data['tags']
            if 'notes' in data:
                expense.notes = data['notes']
            
            # Update budget if amount or category changed
            month = expense.date.strftime('%Y-%m')
            
            if old_category != expense.category or old_amount != expense.amount:
                # Remove from old budget
                old_budget = Budget.query.filter_by(
                    user_id=current_user.id,
                    month=month,
                    category=old_category
                ).first()
                if old_budget:
                    old_budget.spent_amount -= old_amount
                
                # Add to new budget
                new_budget = Budget.query.filter_by(
                    user_id=current_user.id,
                    month=month,
                    category=expense.category
                ).first()
                if new_budget:
                    new_budget.spent_amount += expense.amount
            
            db.session.commit()
            
            return jsonify({
                'message': 'Expense updated successfully',
                'expense': expense.to_dict()
            }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Expense manage error: {e}")
        return jsonify({'error': 'Failed to manage expense'}), 500

# ============================================================================
# API ROUTES - INCOME MANAGEMENT
# ============================================================================

@app.route('/api/income/add', methods=['POST'])
@login_required
def api_add_income():
    """Add income record"""
    try:
        data = request.get_json()
        
        income = Income(
            user_id=current_user.id,
            month=data.get('month'),
            source=data.get('source'),
            amount=float(data.get('amount')),
            description=data.get('description', ''),
            is_recurring=data.get('is_recurring', False),
            received_date=datetime.strptime(data.get('received_date'), '%Y-%m-%d').date() if data.get('received_date') else None
        )
        
        db.session.add(income)
        db.session.commit()
        
        logger.info(f"✓ Income added: ₹{income.amount} - {income.source}")
        
        return jsonify({
            'message': 'Income added successfully',
            'income': income.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Income add error: {e}")
        return jsonify({'error': 'Failed to add income'}), 500

@app.route('/api/income', methods=['GET'])
@login_required
def api_get_income():
    """Get income records"""
    try:
        month = request.args.get('month')
        
        query = Income.query.filter_by(user_id=current_user.id)
        
        if month:
            query = query.filter_by(month=month)
        
        query = query.order_by(Income.created_at.desc())
        
        incomes = query.all()
        
        return jsonify({
            'incomes': [inc.to_dict() for inc in incomes],
            'total': sum(inc.amount for inc in incomes)
        }), 200
        
    except Exception as e:
        logger.error(f"Income get error: {e}")
        return jsonify({'error': 'Failed to load income'}), 500

@app.route('/api/income/<int:income_id>', methods=['PUT', 'DELETE'])
@login_required
def api_manage_income(income_id):
    """Update or delete income record"""
    try:
        income = Income.query.filter_by(
            id=income_id,
            user_id=current_user.id
        ).first()
        
        if not income:
            return jsonify({'error': 'Income not found'}), 404
        
        if request.method == 'DELETE':
            db.session.delete(income)
            db.session.commit()
            return jsonify({'message': 'Income deleted successfully'}), 200
        
        else:  # PUT
            data = request.get_json()
            
            if 'source' in data:
                income.source = data['source']
            if 'amount' in data:
                income.amount = float(data['amount'])
            if 'description' in data:
                income.description = data['description']
            if 'is_recurring' in data:
                income.is_recurring = data['is_recurring']
            
            db.session.commit()
            
            return jsonify({
                'message': 'Income updated successfully',
                'income': income.to_dict()
            }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Income manage error: {e}")
        return jsonify({'error': 'Failed to manage income'}), 500

# ============================================================================
# API ROUTES - DATABASE VIEWER (ADMIN)
# ============================================================================

@app.route('/admin/db-viewer')
@login_required
def db_viewer():
    """Database viewer page"""
    return render_template('admin/db-viewer.html')

@app.route('/api/database/stats', methods=['GET'])
@login_required
def api_database_stats():
    """Get database statistics"""
    try:
        stats = {
            'users': User.query.count(),
            'budgets': Budget.query.count(),
            'expenses': Expense.query.count(),
            'incomes': Income.query.count(),
            'chat_history': ChatHistory.query.count(),
            'banks': Bank.query.count(),
            'insurance_companies': InsuranceCompany.query.count(),
            'investment_funds': InvestmentFund.query.count()
        }
        return jsonify(stats), 200
    except Exception as e:
        logger.error(f"Database stats error: {e}")
        return jsonify({'error': 'Failed to load stats'}), 500

@app.route('/api/database/table/<table_name>', methods=['GET'])
@login_required
def api_get_table_data(table_name):
    """Get data from a specific table"""
    try:
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 50, type=int)
        user_id_filter = request.args.get('user_id', type=int)
        
        # Map table names to models
        table_models = {
            'users': User,
            'budgets': Budget,
            'expenses': Expense,
            'incomes': Income,
            'chat_history': ChatHistory,
            'banks': Bank,
            'insurance_companies': InsuranceCompany,
            'investment_funds': InvestmentFund
        }
        
        if table_name not in table_models:
            return jsonify({'error': 'Invalid table name'}), 400
        
        model = table_models[table_name]
        query = model.query
        
        # Apply user filter if applicable and requested
        if user_id_filter and hasattr(model, 'user_id'):
            query = query.filter_by(user_id=user_id_filter)
        
        # Get total count
        total = query.count()
        
        # Paginate
        offset = (page - 1) * limit
        items = query.limit(limit).offset(offset).all()
        
        # Convert to dict
        data = []
        for item in items:
            if hasattr(item, 'to_dict'):
                data.append(item.to_dict())
            else:
                # Fallback for models without to_dict
                item_dict = {}
                for column in item.__table__.columns:
                    value = getattr(item, column.name)
                    if isinstance(value, datetime):
                        value = value.isoformat()
                    elif isinstance(value, date):
                        value = value.isoformat()
                    item_dict[column.name] = value
                data.append(item_dict)
        
        return jsonify({
            'data': data,
            'total': total,
            'page': page,
            'limit': limit
        }), 200
        
    except Exception as e:
        logger.error(f"Table data error: {e}")
        return jsonify({'error': str(e)}), 500

# ============================================================================
# API ROUTES - ENHANCED AI CHAT
# ============================================================================

@app.route('/api/chat/message', methods=['POST'])
@login_required
def api_chat_message():
    """Process AI chat message with typing delay"""
    start_time = time.time()
    
    try:
        if not conversation_manager:
            return jsonify({
                'error': 'AI Assistant is currently unavailable',
                'message': 'The AI service is not initialized. Please contact support.'
            }), 503
        
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Sanitize and validate input
        message = sanitize_user_input(data.get('message', ''), Config.MAX_MESSAGE_LENGTH)
        session_id = data.get('session_id', f'session_{current_user.id}_{int(datetime.utcnow().timestamp())}')
        
        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        if not validate_session_id(session_id):
            return jsonify({'error': 'Invalid session ID'}), 400
        
        # Get AI response
        logger.info(f"💬 User {current_user.email}: {message[:50]}...")
        
        response = conversation_manager.process_message(message, current_user.id, session_id)
        
        # Calculate typing delay
        response_text = response.get('message', '')
        typing_delay = 0.0
        
        if Config.ENABLE_TYPING_DELAY:
            typing_delay = simulate_typing_delay(
                response_text,
                enabled=True,
                wpm=Config.TYPING_WPM,
                min_delay=Config.TYPING_DELAY_MIN,
                max_delay=Config.TYPING_DELAY_MAX
            )
        
        # Calculate total response time
        total_response_time = calculate_response_time(start_time)
        
        # Save to database
        try:
            chat = ChatHistory(
                user_id=current_user.id,
                session_id=session_id,
                message=message,
                response=response_text,
                tool_used=response.get('tool_used'),
                response_time=total_response_time
            )
            db.session.add(chat)
            db.session.commit()
            
            logger.info(f"✓ Chat saved - Tool: {response.get('tool_used', 'None')}, Time: {total_response_time}s, Delay: {typing_delay}s")
            
        except Exception as e:
            logger.error(f"Failed to save chat: {e}")
            db.session.rollback()
        
        # Add metadata to response
        response['response_time'] = total_response_time
        response['typing_delay'] = typing_delay
        response['session_id'] = session_id
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Chat error: {e}")
        return jsonify({
            'error': 'Chat processing failed',
            'message': 'I apologize, but I encountered an error. Please try again.'
        }), 500

@app.route('/api/chat/history', methods=['GET'])
@login_required
def api_chat_history():
    """Get user's chat history with pagination"""
    try:
        # Get pagination parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('limit', Config.DEFAULT_PAGE_SIZE, type=int)
        per_page = min(per_page, Config.MAX_PAGE_SIZE)
        
        session_id = request.args.get('session_id')
        
        # Build query
        query = ChatHistory.query.filter_by(user_id=current_user.id)
        
        if session_id:
            query = query.filter_by(session_id=session_id)
        
        query = query.order_by(ChatHistory.created_at.desc())
        
        # Paginate
        result = paginate_query(query, page, per_page)
        
        # Format response
        chats = [chat.to_dict() for chat in result['items']]
        
        return jsonify({
            'chats': chats,
            'pagination': result['pagination']
        }), 200
        
    except Exception as e:
        logger.error(f"Chat history error: {e}")
        return jsonify({'error': 'Failed to load chat history'}), 500

@app.route('/api/chat/sessions', methods=['GET'])
@login_required
def api_chat_sessions():
    """Get list of chat sessions with metadata"""
    try:
        # Get unique session IDs with aggregated data
        sessions_query = db.session.query(
            ChatHistory.session_id,
            db.func.count(ChatHistory.id).label('message_count'),
            db.func.min(ChatHistory.created_at).label('created_at'),
            db.func.max(ChatHistory.created_at).label('last_message')
        ).filter_by(user_id=current_user.id)\
         .group_by(ChatHistory.session_id)\
         .order_by(db.desc('last_message'))\
         .limit(50)\
         .all()
        
        sessions = []
        for s in sessions_query:
            # Get first message for preview
            first_msg = ChatHistory.query.filter_by(
                user_id=current_user.id,
                session_id=s.session_id
            ).order_by(ChatHistory.created_at.asc()).first()
            
            sessions.append({
                'session_id': s.session_id,
                'title': get_session_title(first_msg.message) if first_msg else 'New Conversation',
                'message_count': s.message_count,
                'created_at': format_timestamp(s.created_at),
                'last_message_at': format_timestamp(s.last_message),
                'preview': first_msg.message[:100] if first_msg else ''
            })
        
        return jsonify({
            'sessions': sessions,
            'total': len(sessions)
        }), 200
        
    except Exception as e:
        logger.error(f"Sessions error: {e}")
        return jsonify({'error': 'Failed to load sessions'}), 500

@app.route('/api/chat/sessions/delete/<session_id>', methods=['DELETE'])
@login_required
def api_delete_session(session_id):
    """Delete a specific chat session"""
    try:
        if not validate_session_id(session_id):
            return jsonify({'error': 'Invalid session ID'}), 400
        
        # Delete all messages in the session
        deleted = ChatHistory.query.filter_by(
            user_id=current_user.id,
            session_id=session_id
        ).delete()
        
        db.session.commit()
        
        logger.info(f"✓ Deleted session {session_id} for user {current_user.email} ({deleted} messages)")
        
        return jsonify({
            'message': 'Session deleted successfully',
            'deleted_messages': deleted
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Delete session error: {e}")
        return jsonify({'error': 'Failed to delete session'}), 500

@app.route('/api/chat/history/clear', methods=['POST'])
@login_required
def api_clear_history():
    """Clear all chat history for the current user"""
    try:
        deleted = ChatHistory.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        
        logger.info(f"✓ Cleared all history for user {current_user.email} ({deleted} messages)")
        
        return jsonify({
            'message': 'All chat history cleared successfully',
            'deleted_messages': deleted
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Clear history error: {e}")
        return jsonify({'error': 'Failed to clear history'}), 500

@app.route('/api/chat/session/<session_id>/context', methods=['GET'])
@login_required
def api_session_context(session_id):
    """Get conversation context for a session"""
    try:
        if not validate_session_id(session_id):
            return jsonify({'error': 'Invalid session ID'}), 400
        
        limit = request.args.get('limit', Config.DEFAULT_HISTORY_LIMIT, type=int)
        limit = min(limit, Config.MAX_HISTORY_LIMIT)
        
        context = get_conversation_context(session_id, current_user.id, limit)
        metadata = get_session_metadata(session_id, current_user.id)
        
        return jsonify({
            'session_id': session_id,
            'metadata': metadata,
            'context': context,
            'context_length': len(context)
        }), 200
        
    except Exception as e:
        logger.error(f"Session context error: {e}")
        return jsonify({'error': 'Failed to load session context'}), 500

# ============================================================================
# API ROUTES - LOANS
# ============================================================================

@app.route('/api/loans/calculate-emi', methods=['POST'])
def api_calculate_emi():
    """Calculate EMI"""
    try:
        data = request.get_json()
        
        principal = float(data.get('principal', 0))
        rate = float(data.get('rate', 0))
        tenure = float(data.get('tenure', 0))
        
        if principal <= 0 or rate <= 0 or tenure <= 0:
            return jsonify({'error': 'Invalid input values'}), 400
        
        # EMI calculation
        monthly_rate = rate / 12 / 100
        emi = principal * monthly_rate * ((1 + monthly_rate) ** tenure) / (((1 + monthly_rate) ** tenure) - 1)
        
        total_amount = emi * tenure
        total_interest = total_amount - principal
        
        return jsonify({
            'emi': round(emi, 2),
            'total_amount': round(total_amount, 2),
            'total_interest': round(total_interest, 2),
            'principal': principal,
            'rate': rate,
            'tenure': tenure
        }), 200
        
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input format'}), 400
    except Exception as e:
        logger.error(f"EMI calculation error: {e}")
        return jsonify({'error': 'Calculation failed'}), 500

# ============================================================================
# API ROUTES - BANKS DATA
# ============================================================================

@app.route('/api/banks/top20', methods=['GET'])
def api_get_top_banks():
    """Get Top 20 banks"""
    try:
        banks = Bank.query.order_by(Bank.rating.desc()).limit(20).all()
        
        return jsonify([{
            'id': bank.id,
            'name': bank.name,
            'logo_url': bank.logo_url,
            'personal_loan_rate': bank.personal_loan_rate,
            'home_loan_rate': bank.home_loan_rate,
            'car_loan_rate': bank.car_loan_rate,
            'education_loan_rate': bank.education_loan_rate,
            'business_loan_rate': bank.business_loan_rate,
            'savings_rate': bank.savings_rate,
            'fd_rate': bank.fd_rate,
            'processing_fee': bank.processing_fee_percentage,
            'min_loan': bank.min_loan_amount,
            'max_loan': bank.max_loan_amount,
            'rating': bank.rating,
            'customer_support': bank.customer_support,
            'website': bank.website
        } for bank in banks]), 200
        
    except Exception as e:
        logger.error(f"Error fetching banks: {e}")
        return jsonify({'error': 'Failed to load bank data'}), 500

@app.route('/api/banks/<int:bank_id>', methods=['GET'])
def api_get_bank_details(bank_id):
    """Get bank details"""
    try:
        bank = Bank.query.get(bank_id)
        if not bank:
            return jsonify({'error': 'Bank not found'}), 404
        
        return jsonify(bank.to_dict()), 200
        
    except Exception as e:
        logger.error(f"Error fetching bank details: {e}")
        return jsonify({'error': 'Failed to load bank details'}), 500

# ============================================================================
# API ROUTES - INSURANCE DATA
# ============================================================================

@app.route('/api/insurance/companies/top10', methods=['GET'])
def api_get_top_insurance():
    """Get Top 10 insurance companies"""
    try:
        companies = InsuranceCompany.query.order_by(
            InsuranceCompany.claim_settlement_ratio.desc()
        ).limit(10).all()
        
        return jsonify([{
            'id': company.id,
            'name': company.name,
            'logo_url': company.logo_url,
            'life_premium_start': company.life_premium_start,
            'health_premium_start': company.health_premium_start,
            'car_premium_start': company.car_premium_start,
            'claim_settlement_ratio': company.claim_settlement_ratio,
            'death_benefit_max': company.death_benefit_max,
            'hospital_coverage_max': company.hospital_coverage_max,
            'cashless_hospitals': company.cashless_hospitals,
            'rating': company.rating,
            'customer_support': company.customer_support,
            'website': company.website
        } for company in companies]), 200
        
    except Exception as e:
        logger.error(f"Error fetching insurance companies: {e}")
        return jsonify({'error': 'Failed to load insurance data'}), 500

@app.route('/api/insurance/companies/<int:company_id>', methods=['GET'])
def api_get_insurance_details(company_id):
    """Get insurance company details"""
    try:
        company = InsuranceCompany.query.get(company_id)
        if not company:
            return jsonify({'error': 'Insurance company not found'}), 404
        
        return jsonify(company.to_dict()), 200
        
    except Exception as e:
        logger.error(f"Error fetching insurance details: {e}")
        return jsonify({'error': 'Failed to load insurance details'}), 500

# ============================================================================
# API ROUTES - INVESTMENT FUNDS DATA
# ============================================================================

@app.route('/api/investments/funds/top10', methods=['GET'])
def api_get_top_funds():
    """Get Top 10 investment funds"""
    try:
        funds = InvestmentFund.query.order_by(
            InvestmentFund.returns_5yr.desc()
        ).limit(10).all()
        
        return jsonify([{
            'id': fund.id,
            'fund_name': fund.fund_name,
            'fund_type': fund.fund_type,
            'amc_name': fund.amc_name,
            'nav': fund.nav,
            'returns_1yr': fund.returns_1yr,
            'returns_3yr': fund.returns_3yr,
            'returns_5yr': fund.returns_5yr,
            'expense_ratio': fund.expense_ratio,
            'min_investment': fund.min_investment,
            'min_sip': fund.min_sip,
            'risk_level': fund.risk_level,
            'rating': fund.rating,
            'description': fund.description
        } for fund in funds]), 200
        
    except Exception as e:
        logger.error(f"Error fetching investment funds: {e}")
        return jsonify({'error': 'Failed to load fund data'}), 500

@app.route('/api/investments/funds/<int:fund_id>', methods=['GET'])
def api_get_fund_details(fund_id):
    """Get fund details"""
    try:
        fund = InvestmentFund.query.get(fund_id)
        if not fund:
            return jsonify({'error': 'Fund not found'}), 404
        
        return jsonify(fund.to_dict()), 200
        
    except Exception as e:
        logger.error(f"Error fetching fund details: {e}")
        return jsonify({'error': 'Failed to load fund details'}), 500

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(e):
    """404 error handler"""
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Endpoint not found'}), 404
    return render_template('1-login.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """500 error handler"""
    logger.error(f"Internal error: {e}")
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Internal server error'}), 500
    return render_template('1-login.html'), 500

@app.errorhandler(401)
def unauthorized(e):
    """401 error handler"""
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Unauthorized - Please login'}), 401
    return redirect(url_for('index'))

# ============================================================================
# DATABASE INITIALIZATION
# ============================================================================

def init_database():
    """Initialize database with tables and seed data"""
    try:
        with app.app_context():
            db.create_all()
            logger.info("✓ Database initialized successfully")
            
            # Seed data if tables are empty
            if Bank.query.count() == 0:
                logger.info("📝 Seeding database with initial data...")
                from database.seed_data import seed_all_data
                seed_all_data(db, Bank, InsuranceCompany, InvestmentFund)
            else:
                logger.info(f"✓ Database contains: {Bank.query.count()} banks, {InsuranceCompany.query.count()} insurance companies, {InvestmentFund.query.count()} funds")
            
            return True
    except Exception as e:
        logger.error(f"✗ Database initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# APPLICATION STARTUP
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🏦  CredNest AI - Ultra Premium Finance Platform")
    print("="*70)
    
    # Initialize database
    db_status = init_database()
    print(f"💾  Database: {'✓ Ready' if db_status else '✗ Failed'}")
    
    # Initialize AI
    ai_status = init_finance_ai()
    print(f"🤖  Finance AI: {'✓ Active' if ai_status else '✗ Offline (check GROQ_API_KEY)'}")
    
    # Display configuration
    print(f"⚙️   Typing Delay: {'✓ Enabled' if Config.ENABLE_TYPING_DELAY else '✗ Disabled'}")
    if Config.ENABLE_TYPING_DELAY:
        print(f"    └─ Range: {Config.TYPING_DELAY_MIN}s - {Config.TYPING_DELAY_MAX}s @ {Config.TYPING_WPM} WPM")
    
    print(f"🌐  Server: http://localhost:5000")
    print(f"📊  Status: {'✓ All systems operational' if db_status and ai_status else '⚠️  Partial functionality'}")
    print("="*70)
    print("\n📱  Available Pages:")
    print("   → /                  - Login page")
    print("   → /dashboard         - Main dashboard")
    print("   → /budgeting         - Budget planner")
    print("   → /savings           - Savings goals")
    print("   → /investments       - Investment portfolio")
    print("   → /loans             - Loan comparison")
    print("   → /insurance         - Insurance comparison")
    print("   → /chat              - AI Finance Assistant")
    print("   → /profile           - User profile")
    print("   → /about             - About page")
    print("   → /contact           - Contact page")
    print("\n💡  Tip: Register a new account or login with existing credentials")
    print("="*70 + "\n")
    
    # Run Flask app
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=True
    )
