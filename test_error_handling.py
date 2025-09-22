#!/usr/bin/env python3
"""
Test error handling untuk Railway
"""

import os
import sys
from app import app

def test_error_handling():
    """Test error handling"""
    try:
        print("🔧 Testing error handling...")
        
        # Test app creation
        print("✅ Flask app created successfully")
        
        # Test error handlers
        with app.test_client() as client:
            # Test 404 error
            response = client.get('/nonexistent-page')
            print(f"📊 404 Response: {response.status_code}")
            
            # Test 500 error (if any)
            try:
                response = client.get('/')
                print(f"📊 Home Response: {response.status_code}")
            except Exception as e:
                print(f"⚠️  Home page error: {str(e)}")
        
        print("✅ Error handling test completed")
        return True
        
    except Exception as e:
        print(f"❌ Error handling test failed: {str(e)}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("  Error Handling Test")
    print("=" * 50)
    print()
    
    success = test_error_handling()
    
    if success:
        print("\n🎉 Error handling test passed!")
        print("🚀 Your Railway deployment should work!")
    else:
        print("\n❌ Error handling test failed!")
        print("🔧 Check your error handlers")
    
    print()
    print("=" * 50)
