"""
CredNest AI - Utility Functions
Helper functions for chat, pagination, and common operations
"""

import time
import re
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def calculate_typing_delay(text: str, wpm: int = 200, min_delay: float = 0.5, max_delay: float = 3.0) -> float:
    """
    Calculate natural typing delay based on text length
    
    Args:
        text: The text to calculate delay for
        wpm: Words per minute typing speed (default: 200)
        min_delay: Minimum delay in seconds
        max_delay: Maximum delay in seconds
    
    Returns:
        Delay in seconds
    """
    if not text:
        return min_delay
    
    # Count words
    words = len(text.split())
    
    # Calculate delay based on WPM
    # Convert WPM to words per second, then to seconds per word
    delay = (words / wpm) * 60
    
    # Clamp between min and max
    delay = max(min_delay, min(delay, max_delay))
    
    return round(delay, 2)


def simulate_typing_delay(text: str, enabled: bool = True, **kwargs) -> float:
    """
    Simulate typing delay and return the delay time
    
    Args:
        text: The text being "typed"
        enabled: Whether delay is enabled
        **kwargs: Additional arguments for calculate_typing_delay
    
    Returns:
        Actual delay time in seconds
    """
    if not enabled:
        return 0.0
    
    delay = calculate_typing_delay(text, **kwargs)
    time.sleep(delay)
    return delay


def paginate_query(query, page: int = 1, per_page: int = 20) -> Dict[str, Any]:
    """
    Paginate a SQLAlchemy query
    
    Args:
        query: SQLAlchemy query object
        page: Page number (1-indexed)
        per_page: Items per page
    
    Returns:
        Dictionary with pagination metadata and items
    """
    # Ensure valid page number
    page = max(1, page)
    per_page = min(100, max(1, per_page))  # Cap at 100 items per page
    
    # Get total count
    total = query.count()
    
    # Calculate pagination
    total_pages = (total + per_page - 1) // per_page  # Ceiling division
    has_prev = page > 1
    has_next = page < total_pages
    
    # Get items for current page
    items = query.limit(per_page).offset((page - 1) * per_page).all()
    
    return {
        'items': items,
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'total_pages': total_pages,
            'has_prev': has_prev,
            'has_next': has_next,
            'prev_page': page - 1 if has_prev else None,
            'next_page': page + 1 if has_next else None
        }
    }


def sanitize_user_input(text: str, max_length: int = 2000) -> str:
    """
    Sanitize user input text
    
    Args:
        text: Input text to sanitize
        max_length: Maximum allowed length
    
    Returns:
        Sanitized text
    """
    if not text:
        return ""
    
    # Strip whitespace
    text = text.strip()
    
    # Truncate if too long
    if len(text) > max_length:
        text = text[:max_length]
    
    # Remove any null bytes
    text = text.replace('\x00', '')
    
    return text


def format_chat_session(session_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format chat session data for API response
    
    Args:
        session_data: Raw session data from database
    
    Returns:
        Formatted session data
    """
    return {
        'session_id': session_data.get('session_id'),
        'message_count': session_data.get('message_count', 0),
        'last_message_at': session_data.get('last_message'),
        'created_at': session_data.get('created_at'),
        'preview': session_data.get('preview', '')[:100]  # First 100 chars
    }


def get_session_title(first_message: str, max_length: int = 50) -> str:
    """
    Generate a session title from the first message
    
    Args:
        first_message: The first message in the session
        max_length: Maximum title length
    
    Returns:
        Session title
    """
    if not first_message:
        return "New Conversation"
    
    # Clean the message
    title = first_message.strip()
    
    # Remove extra whitespace
    title = re.sub(r'\s+', ' ', title)
    
    # Truncate if needed
    if len(title) > max_length:
        title = title[:max_length - 3] + "..."
    
    return title


def format_timestamp(dt: Optional[datetime]) -> Optional[str]:
    """
    Format datetime to ISO string
    
    Args:
        dt: Datetime object
    
    Returns:
        ISO formatted string or None
    """
    if dt is None:
        return None
    return dt.isoformat()


def calculate_response_time(start_time: float) -> float:
    """
    Calculate response time from start time
    
    Args:
        start_time: Start time from time.time()
    
    Returns:
        Response time in seconds
    """
    return round(time.time() - start_time, 3)


def validate_session_id(session_id: str) -> bool:
    """
    Validate session ID format
    
    Args:
        session_id: Session ID to validate
    
    Returns:
        True if valid, False otherwise
    """
    if not session_id:
        return False
    
    # Session ID should be alphanumeric with underscores, reasonable length
    if len(session_id) > 200:
        return False
    
    # Check format
    pattern = r'^[a-zA-Z0-9_-]+$'
    return bool(re.match(pattern, session_id))


def chunk_text(text: str, chunk_size: int = 1000) -> List[str]:
    """
    Split text into chunks of specified size
    
    Args:
        text: Text to chunk
        chunk_size: Maximum chunk size
    
    Returns:
        List of text chunks
    """
    if not text:
        return []
    
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    
    return chunks


def truncate_history(history: List[Dict], max_messages: int = 10) -> List[Dict]:
    """
    Truncate conversation history to recent messages
    
    Args:
        history: List of conversation messages
        max_messages: Maximum number of messages to keep
    
    Returns:
        Truncated history
    """
    if len(history) <= max_messages:
        return history
    
    # Keep most recent messages
    return history[-max_messages:]


def format_error_response(error_message: str, status_code: int = 500) -> Dict[str, Any]:
    """
    Format error response for API
    
    Args:
        error_message: Error message
        status_code: HTTP status code
    
    Returns:
        Formatted error response
    """
    return {
        'error': error_message,
        'status': 'error',
        'timestamp': datetime.utcnow().isoformat()
    }


def log_api_call(endpoint: str, user_id: Optional[int] = None, **kwargs):
    """
    Log API call with metadata
    
    Args:
        endpoint: API endpoint
        user_id: User ID if available
        **kwargs: Additional metadata
    """
    metadata = {
        'endpoint': endpoint,
        'user_id': user_id,
        'timestamp': datetime.utcnow().isoformat(),
        **kwargs
    }
    logger.info(f"API Call: {metadata}")
