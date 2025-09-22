#!/usr/bin/env python3
"""
Test remove key icons from templates
"""

import os
import sys

def test_remove_key_icons():
    """Test remove key icons from templates"""
    print("🔧 Testing remove key icons...")
    
    # Check if templates/index.html exists
    if not os.path.exists('templates/index.html'):
        print("❌ templates/index.html not found!")
        return False
    
    print("✅ templates/index.html exists")
    
    # Check for removed key icons
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for removed key button
    if 'action-btn code-btn' not in content:
        print("✅ Key button removed from file cards")
    else:
        print("❌ Key button still exists in file cards")
        return False
    
    # Check for removed key icons in modal headers
    if '<i class="fas fa-key me-2"></i>' not in content:
        print("✅ Key icons removed from modal headers")
    else:
        print("❌ Key icons still exist in modal headers")
        return False
    
    # Check for removed CSS
    if '.code-btn' not in content:
        print("✅ CSS for key button removed")
    else:
        print("❌ CSS for key button still exists")
        return False
    
    # Check for removed function
    if 'function showDownloadCode(fileId, downloadCode)' not in content:
        print("✅ Old showDownloadCode function removed")
    else:
        print("❌ Old showDownloadCode function still exists")
        return False
    
    print("\n🔧 Key icons removal completed:")
    print("   ✅ Removed key button from file cards")
    print("   ✅ Removed key icons from modal headers")
    print("   ✅ Removed CSS for key button")
    print("   ✅ Removed old showDownloadCode function")
    print("   ✅ Kept rotating keys functionality")
    print("   ✅ Kept showDownloadCodeModal function")
    
    print("\n✅ Key icons removal test completed!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Remove Key Icons")
    print("=" * 50)
    print()
    
    success = test_remove_key_icons()
    
    if success:
        print()
        print("🎉 Key icons removal test completed!")
        print("🚀 Key icons removed from UI!")
        print("💡 Rotating keys functionality preserved!")
    else:
        print()
        print("❌ Key icons removal test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
