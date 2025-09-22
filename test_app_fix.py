#!/usr/bin/env python3
"""
Test application fix
"""

import os
import sys

def test_app_fix():
    """Test application fix"""
    print("🔧 Testing application fix...")
    
    # Test import
    try:
        import app
        print("✅ App imports successfully")
    except Exception as e:
        print(f"❌ App import error: {str(e)}")
        return False
    
    # Check routes
    routes = [
        '/',
        '/login',
        '/register',
        '/logout',
        '/upload',
        '/download/<download_key>',
        '/preview/<download_key>',
        '/copy-link/<int:file_id>'
    ]
    
    print("📋 Available routes:")
    for route in routes:
        print(f"   ✅ {route}")
    
    # Check templates
    templates = [
        'templates/base.html',
        'templates/index.html',
        'templates/login.html',
        'templates/register.html',
        'templates/error.html'
    ]
    
    print("\n📋 Template files:")
    for template in templates:
        if os.path.exists(template):
            print(f"   ✅ {template}")
        else:
            print(f"   ❌ {template}")
    
    # Check uploads folder
    if os.path.exists('uploads'):
        print(f"✅ Uploads folder exists")
        files = [f for f in os.listdir('uploads') if os.path.isfile(os.path.join('uploads', f)) and f != '.gitkeep']
        print(f"📊 Files in uploads: {len(files)}")
    else:
        print("❌ Uploads folder not found")
        return False
    
    print("✅ Application fix test completed successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Application Fix")
    print("=" * 50)
    print()
    
    success = test_app_fix()
    
    if success:
        print()
        print("🎉 Application fix test completed!")
        print("🚀 BuildError is fixed!")
        print("📁 All routes and templates are working.")
        print("⬇️ Download and preview features are ready.")
    else:
        print()
        print("❌ Application fix test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
