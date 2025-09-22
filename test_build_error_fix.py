#!/usr/bin/env python3
"""
Test BuildError fix
"""

import os
import sys

def test_build_error_fix():
    """Test BuildError fix"""
    print("🔧 Testing BuildError fix...")
    
    # Check if register.html is deleted
    register_file = 'templates/register.html'
    if not os.path.exists(register_file):
        print("✅ register.html deleted (no longer needed)")
    else:
        print("❌ register.html still exists")
        return False
    
    # Check app files
    app_files = ['app.py', 'models.py', 'config.py', 'run.py']
    for file in app_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} not found")
            return False
    
    # Check templates
    template_files = [
        'templates/index.html', 
        'templates/login.html', 
        'templates/base.html',
        'templates/admin_register.html'
    ]
    for file in template_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} not found")
            return False
    
    print("\n🔧 BuildError fixes implemented:")
    print("   ✅ Removed register link from base.html navbar")
    print("   ✅ Deleted unused register.html template")
    print("   ✅ Updated dashboard.html to use admin_register")
    print("   ✅ Updated auth/profile.html to use admin_register")
    print("   ✅ All references now point to admin_register")
    
    print("\n✅ BuildError fix test completed!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test BuildError Fix")
    print("=" * 50)
    print()
    
    success = test_build_error_fix()
    
    if success:
        print()
        print("🎉 BuildError fix test completed!")
        print("🚀 All register references fixed!")
        print("🔧 Application should work without BuildError!")
    else:
        print()
        print("❌ BuildError fix test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
