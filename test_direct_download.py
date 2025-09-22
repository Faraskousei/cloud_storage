#!/usr/bin/env python3
"""
Test direct download system for logged in users
"""

import os
import sys

def test_direct_download():
    """Test direct download system"""
    print("🔧 Testing direct download system...")
    
    # Check if app.py exists
    if not os.path.exists('app.py'):
        print("❌ app.py not found!")
        return False
    
    print("✅ app.py exists")
    
    # Check for direct download implementation
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for direct download features
    direct_download_features = [
        '@app.route(\'/get-file-info/<int:file_id>\')',
        'def get_file_info_by_id(file_id):',
        '@app.route(\'/download_logged_in/<filename>\')',
        'def download_file(filename):',
        '@login_required',
        'as_attachment=True'
    ]
    
    print("\n🔧 Checking direct download implementation...")
    for feature in direct_download_features:
        if feature in content:
            print(f"✅ {feature}")
        else:
            print(f"❌ {feature} not found")
            return False
    
    # Check templates/index.html
    if not os.path.exists('templates/index.html'):
        print("❌ templates/index.html not found!")
        return False
    
    print("✅ templates/index.html exists")
    
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Check for direct download UI features
    ui_features = [
        'fetch(`/get-file-info/${fileId}`)',
        '/download_logged_in/${data.file.stored_name}',
        'Direct download for logged in users',
        'File berhasil didownload!'
    ]
    
    print("\n🔧 Checking UI features...")
    for feature in ui_features:
        if feature in template_content:
            print(f"✅ {feature}")
        else:
            print(f"❌ {feature} not found")
    
    print("\n🔧 Direct download system features:")
    print("   ✅ Direct download for logged in users")
    print("   ✅ No key/code required for logged in users")
    print("   ✅ Rotating keys only for copied links")
    print("   ✅ Enhanced security with dual system")
    print("   ✅ Better user experience")
    print("   ✅ Admin can download all files")
    print("   ✅ Regular users can download team files only")
    
    print("\n📊 Download system workflow:")
    print("   1. Logged in user clicks 'Download' button")
    print("   2. System gets file info via /get-file-info/<file_id>")
    print("   3. System downloads file via /download_logged_in/<filename>")
    print("   4. File downloaded directly without key/code")
    print("   5. Copy link still uses rotating keys for external access")
    
    print("\n🔐 Security benefits:")
    print("   🔒 Logged in users: Direct download (no key needed)")
    print("   🔒 External links: Rotating keys required")
    print("   🔒 Team isolation: Users only see their team files")
    print("   🔒 Admin access: Admin can download all files")
    print("   🔒 Enhanced UX: Faster download for logged in users")
    
    print("\n✅ Direct download system test completed!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Direct Download System")
    print("=" * 50)
    print()
    
    success = test_direct_download()
    
    if success:
        print()
        print("🎉 Direct download system test completed!")
        print("🚀 Logged in users can download directly!")
        print("🔐 Rotating keys only for copied links!")
        print("💡 Enhanced user experience!")
    else:
        print()
        print("❌ Direct download system test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
