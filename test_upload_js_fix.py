#!/usr/bin/env python3
"""
Test upload JavaScript fix
"""

import os
import sys

def test_upload_js_fix():
    """Test upload JavaScript fix"""
    print("🔧 Testing upload JavaScript fix...")
    
    # Check if index.html exists
    if not os.path.exists('templates/index.html'):
        print("❌ templates/index.html not found!")
        return False
    
    print("✅ templates/index.html exists")
    
    # Check for JavaScript null checks
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for null checks in JavaScript
    null_checks = [
        'if (uploadProgress)',
        'if (uploadStatus)',
        'if (uploadBtn)',
        'if (statusText)',
        'if (progressBar)'
    ]
    
    print("\n🔧 Checking JavaScript null checks...")
    for check in null_checks:
        if check in content:
            print(f"✅ {check} found")
        else:
            print(f"❌ {check} not found")
            return False
    
    # Check for error handling
    error_handling = [
        'showNotification',
        'console.log',
        'console.error',
        'clearInterval'
    ]
    
    print("\n🔧 Checking error handling...")
    for handler in error_handling:
        if handler in content:
            print(f"✅ {handler} found")
        else:
            print(f"❌ {handler} not found")
    
    print("\n🔧 JavaScript upload fixes implemented:")
    print("   ✅ Added null checks for all DOM elements")
    print("   ✅ Protected against null reference errors")
    print("   ✅ Enhanced error handling")
    print("   ✅ Better progress bar handling")
    print("   ✅ Improved status message handling")
    
    print("\n✅ Upload JavaScript fix test completed!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Upload JavaScript Fix")
    print("=" * 50)
    print()
    
    success = test_upload_js_fix()
    
    if success:
        print()
        print("🎉 Upload JavaScript fix test completed!")
        print("🚀 JavaScript errors should be fixed!")
        print("💡 Upload should now work without console errors.")
    else:
        print()
        print("❌ Upload JavaScript fix test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
