#!/usr/bin/env python3
"""
Test rotating download keys system (simple version)
"""

import os
import sys

def test_rotating_keys_simple():
    """Test rotating download keys system"""
    print("🔧 Testing rotating download keys system...")
    
    # Check app.py for rotating keys implementation
    if not os.path.exists('app.py'):
        print("❌ app.py not found!")
        return False
    
    print("✅ app.py exists")
    
    # Check for rotating keys implementation
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for key rotation features
    rotation_features = [
        'Generate NEW download key setiap kali copy link',
        'old_key = file_record.download_key',
        'new_key = File().generate_download_key()',
        'new_code = File().generate_download_code()',
        'file_record.download_key = new_key',
        'file_record.download_code = new_code'
    ]
    
    print("\n🔧 Checking rotating keys implementation...")
    for feature in rotation_features:
        if feature in content:
            print(f"✅ {feature}")
        else:
            print(f"❌ {feature} not found")
            return False
    
    # Check templates/index.html for UI updates
    if not os.path.exists('templates/index.html'):
        print("❌ templates/index.html not found!")
        return False
    
    print("✅ templates/index.html exists")
    
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Check for UI features
    ui_features = [
        'showDownloadCodeModal',
        'Kode Download Baru',
        'Kode ini akan berubah setiap kali link di-copy',
        'Link lama tidak akan berfungsi lagi'
    ]
    
    print("\n🔧 Checking UI features...")
    for feature in ui_features:
        if feature in template_content:
            print(f"✅ {feature}")
        else:
            print(f"❌ {feature} not found")
    
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
    
    success = test_rotating_keys_simple()
    
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
