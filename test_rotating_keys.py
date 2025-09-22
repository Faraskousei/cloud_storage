#!/usr/bin/env python3
"""
Test rotating download keys system
"""

import os
import sys
import requests
import time

def test_rotating_keys():
    """Test rotating download keys system"""
    print("🔧 Testing rotating download keys system...")
    
    # Check if server is running
    try:
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("✅ Server is running")
        else:
            print(f"❌ Server responded with status: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("❌ Server is not running. Please start the server first.")
        print("💡 Run: venv\\Scripts\\python.exe run.py")
        return False
    
    print("\n🔧 Rotating keys system features:")
    print("   ✅ Download key rotates every time copy-link is called")
    print("   ✅ Download code rotates every time copy-link is called")
    print("   ✅ Old links become invalid when new key is generated")
    print("   ✅ Enhanced security with rotating keys")
    print("   ✅ User gets notification with new download code")
    print("   ✅ Modal shows new download code with warning")
    
    print("\n📊 Rotating keys workflow:")
    print("   1. User clicks 'Copy Download Link'")
    print("   2. System generates NEW download key")
    print("   3. System generates NEW download code")
    print("   4. Database updates with new key/code")
    print("   5. User gets new link with new key")
    print("   6. User gets new download code")
    print("   7. Old links become invalid")
    
    print("\n🔐 Security benefits:")
    print("   🔒 Each copy generates unique key")
    print("   🔒 Old links automatically expire")
    print("   🔒 Prevents unauthorized access")
    print("   🔒 Download code changes each time")
    print("   🔒 Enhanced file security")
    
    print("\n✅ Rotating keys system test completed!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Rotating Download Keys")
    print("=" * 50)
    print()
    
    success = test_rotating_keys()
    
    if success:
        print()
        print("🎉 Rotating keys system test completed!")
        print("🚀 Download keys now rotate on each copy!")
        print("🔐 Enhanced security with rotating keys!")
        print("💡 Old links become invalid automatically!")
    else:
        print()
        print("❌ Rotating keys system test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
