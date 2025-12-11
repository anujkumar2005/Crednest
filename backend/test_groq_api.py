"""
Groq API Test Script
Run this to verify your Groq API key is working
"""

from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("\n" + "="*70)
print("🧪 Testing Groq API Connection")
print("="*70)

# Get API key
api_key = os.getenv('GROQ_API_KEY', 'your-groq-api-key-here')

print(f"\n🔑 API Key: {api_key[:20]}...{api_key[-10:]}")

try:
    # Test 1: Initialize client
    print("\n📌 Test 1: Initializing Groq client...")
    client = Groq(api_key=api_key)
    print("✅ Client initialized successfully!")
    
    # Test 2: Simple chat completion
    print("\n📌 Test 2: Sending test message...")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'Hello, I am working!' in one sentence."}
        ],
        temperature=0.5,
        max_tokens=50
    )
    
    message = response.choices[0].message.content
    print(f"✅ Response received: {message}")
    
    # Test 3: Test with tools/function calling
    print("\n📌 Test 3: Testing function calling...")
    tools = [{
        "type": "function",
        "function": {
            "name": "test_function",
            "description": "A test function",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "A test message"}
                },
                "required": ["message"]
            }
        }
    }]
    
    response2 = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": "Call test_function with message 'Testing'"}
        ],
        tools=tools,
        tool_choice="auto",
        temperature=0.5,
        max_tokens=50
    )
    
    print("✅ Function calling test passed!")
    
    print("\n" + "="*70)
    print("🎉 ALL TESTS PASSED - Groq API is working perfectly!")
    print("="*70 + "\n")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\n💡 Possible solutions:")
    print("   1. Check your GROQ_API_KEY in .env file")
    print("   2. Run: pip uninstall groq -y && pip install groq==0.11.0")
    print("   3. Verify API key is valid at https://console.groq.com")
    print("="*70 + "\n")
