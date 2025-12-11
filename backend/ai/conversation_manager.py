"""
CredNest AI - Enhanced Conversation Manager with Memory
Includes conversation history, greeting detection, and finance topic validation
"""

from groq import Groq
import json
import logging
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from ai.chat_utils import (
    is_greeting_or_casual,
    generate_friendly_response,
    is_finance_related,
    get_session_history_from_db,
    build_enhanced_system_prompt
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConversationManager:
    """Enhanced finance AI with conversation memory"""
    
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key required")
        
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"
        self.system_prompt = build_enhanced_system_prompt()
        logger.info("✓ AI initialized with enhanced memory")
    
    def process_message(self, user_message: str, user_id: int = None, session_id: str = None) -> dict:
        """Process message with conversation memory and context"""
        try:
            # Check if greeting/casual conversation
            if is_greeting_or_casual(user_message):
                response_text = generate_friendly_response(user_message)
                return {
                    'message': response_text,
                    'tool_used': 'greeting_handler',
                    'tool_parameters': None,
                    'data': None,
                    'status': 'success'
                }
            
            # Check if finance-related
            if not is_finance_related(user_message):
                response_text = ("I appreciate your question! 😊 However, I specialize in **financial topics only**.\n\n"
                               "I can help you with:\n"
                               "💰 **Loans** - Personal, Home, Car, Education\n"
                               "📊 **CIBIL Scores** - Understanding and improving\n"
                               "💳 **Banking** - Rates, eligibility, comparisons\n"
                               "🧮 **EMI Calculations** - Planning your payments\n"
                               "📄 **Financial Documentation** - What you need\n\n"
                               "Could you ask me a finance-related question? I'd love to help! 💡")
                
                return {
                    'message': response_text,
                    'tool_used': 'topic_filter',
                    'tool_parameters': None,
                    'data': None,
                    'status': 'success'
                }
            
            # Build conversation with history
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # Add conversation history if available
            if session_id and user_id:
                try:
                    history = get_session_history_from_db(session_id, user_id, limit=8)
                    logger.info(f"📚 Retrieved {len(history)} previous messages")
                    
                    for exchange in history:
                        messages.append({"role": "user", "content": exchange['user']})
                        messages.append({"role": "assistant", "content": exchange['assistant']})
                except Exception as e:
                    logger.warning(f"Could not retrieve history: {e}")
            
            # Add current message
            messages.append({"role": "user", "content": user_message})
            
            logger.info(f"🤖 Calling Groq API with {len(messages)} messages...")
            
            # Call Groq API with optimized parameters for detailed responses
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.8,  # Slightly higher for more creative, detailed responses
                max_tokens=4096,  # Increased for comprehensive answers
                top_p=0.95  # Higher for more diverse, detailed outputs
            )
            
            message_content = response.choices[0].message.content
            logger.info(f"✅ Got response: {message_content[:100]}...")
            
            return {
                'message': message_content,
                'tool_used': 'ai_chat',
                'tool_parameters': {'history_length': len(messages) - 2},  # Exclude system and current message
                'data': None,
                'status': 'success'
            }
            
        except Exception as e:
            logger.error(f"Error: {e}")
            return {
                'message': ("I apologize, but I'm experiencing technical difficulties right now. "
                          "Could you please try asking your question again in a moment? 😊\n\n"
                          "In the meantime, you can try our EMI calculator or eligibility checker!"),
                'tool_used': None,
                'tool_parameters': None,
                'data': None,
                'status': 'error',
                'error': str(e)
            }
