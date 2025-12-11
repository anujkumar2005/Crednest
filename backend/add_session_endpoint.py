"""
Add session loading endpoint to app.py
This endpoint loads all messages from a specific session
"""

endpoint_code = '''
@app.route('/api/chat/session/<session_id>', methods=['GET'])
@login_required
def api_get_session(session_id):
    """Get all messages from a specific session"""
    try:
        if not validate_session_id(session_id):
            return jsonify({'error': 'Invalid session ID'}), 400
        
        # Get all messages from the session
        messages = ChatHistory.query.filter_by(
            user_id=current_user.id,
            session_id=session_id
        ).order_by(ChatHistory.created_at.asc()).all()
        
        # Get session metadata
        metadata = get_session_metadata(session_id, current_user.id)
        
        return jsonify({
            'session_id': session_id,
            'metadata': metadata,
            'messages': [
                {
                    'id': msg.id,
                    'message': msg.message,
                    'response': msg.response,
                    'created_at': format_timestamp(msg.created_at)
                }
                for msg in messages
            ],
            'message_count': len(messages)
        }), 200
        
    except Exception as e:
        logger.error(f"Get session error: {e}")
        return jsonify({'error': 'Failed to load session'}), 500

'''

print("Endpoint code to add:")
print(endpoint_code)
print("\nAdd this endpoint after line 1253 in app.py (after the clear history endpoint)")
