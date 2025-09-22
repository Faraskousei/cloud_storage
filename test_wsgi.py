#!/usr/bin/env python3
"""
Test WSGI entry point untuk Railway
"""

import os
import sys

def test_wsgi_import():
    """Test WSGI import"""
    try:
        print("🔧 Testing WSGI import...")
        
        # Test wsgi.py
        try:
            import wsgi
            print("✅ wsgi.py imported successfully")
        except Exception as e:
            print(f"❌ wsgi.py import failed: {str(e)}")
            return False
        
        # Test wsgi_simple.py
        try:
            import wsgi_simple
            print("✅ wsgi_simple.py imported successfully")
        except Exception as e:
            print(f"❌ wsgi_simple.py import failed: {str(e)}")
            return False
        
        # Test app object
        try:
            from wsgi import app
            print("✅ Flask app object accessible")
            print(f"📊 App config: {app.config.get('DEBUG')}")
        except Exception as e:
            print(f"❌ Flask app object failed: {str(e)}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ WSGI test failed: {str(e)}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("  WSGI Entry Point Test")
    print("=" * 50)
    print()
    
    success = test_wsgi_import()
    
    if success:
        print("\n🎉 WSGI test passed!")
        print("🚀 Your Railway deployment should work!")
    else:
        print("\n❌ WSGI test failed!")
        print("🔧 Check your WSGI configuration")
    
    print()
    print("=" * 50)
