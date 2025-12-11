# API Routes for Database Viewer, Profile, Budget, Expense, and Income Management
# Add these routes to app.py

# ============================================================================
# API ROUTES - DATABASE VIEWER (ADMIN)
# ============================================================================

@app.route('/admin/db-viewer')
@login_required
def db_viewer():
    """Database viewer page (admin only)"""
    # TODO: Add admin check
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
# API ROUTES - USER PROFILE
# ============================================================================

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
            from datetime import datetime
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
        
        from datetime import datetime
        
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
            from datetime import datetime
            start_date = datetime.strptime(f"{month}-01", '%Y-%m-%d').date()
            query = query.filter(db.extract('year', Expense.date) == start_date.year,
                               db.extract('month', Expense.date) == start_date.month)
        
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

@app.route('/api/expenses/<int:expense_id>', methods=['PUT'])
@login_required
def api_update_expense(expense_id):
    """Update expense"""
    try:
        expense = Expense.query.filter_by(
            id=expense_id,
            user_id=current_user.id
        ).first()
        
        if not expense:
            return jsonify({'error': 'Expense not found'}), 404
        
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
        logger.error(f"Expense update error: {e}")
        return jsonify({'error': 'Failed to update expense'}), 500

@app.route('/api/expenses/<int:expense_id>', methods=['DELETE'])
@login_required
def api_delete_expense(expense_id):
    """Delete expense"""
    try:
        expense = Expense.query.filter_by(
            id=expense_id,
            user_id=current_user.id
        ).first()
        
        if not expense:
            return jsonify({'error': 'Expense not found'}), 404
        
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
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Expense delete error: {e}")
        return jsonify({'error': 'Failed to delete expense'}), 500

# ============================================================================
# API ROUTES - INCOME MANAGEMENT
# ============================================================================

@app.route('/api/income/add', methods=['POST'])
@login_required
def api_add_income():
    """Add income record"""
    try:
        data = request.get_json()
        
        from datetime import datetime
        
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

@app.route('/api/income/<int:income_id>', methods=['PUT'])
@login_required
def api_update_income(income_id):
    """Update income record"""
    try:
        income = Income.query.filter_by(
            id=income_id,
            user_id=current_user.id
        ).first()
        
        if not income:
            return jsonify({'error': 'Income not found'}), 404
        
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
        logger.error(f"Income update error: {e}")
        return jsonify({'error': 'Failed to update income'}), 500

@app.route('/api/income/<int:income_id>', methods=['DELETE'])
@login_required
def api_delete_income(income_id):
    """Delete income record"""
    try:
        income = Income.query.filter_by(
            id=income_id,
            user_id=current_user.id
        ).first()
        
        if not income:
            return jsonify({'error': 'Income not found'}), 404
        
        db.session.delete(income)
        db.session.commit()
        
        return jsonify({'message': 'Income deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Income delete error: {e}")
        return jsonify({'error': 'Failed to delete income'}), 500
