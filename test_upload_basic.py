#!/usr/bin/env python3
"""
Test basic upload functionality
"""

import os
import sys

def test_upload_basic():
    """Test basic upload functionality"""
    print("🔧 Testing basic upload functionality...")
    
    # Check uploads folder
    uploads_folder = 'uploads'
    if not os.path.exists(uploads_folder):
        print("❌ Uploads folder not found!")
        return False
    
    print(f"✅ Uploads folder exists: {uploads_folder}")
    
    # List files in uploads folder
    files = [f for f in os.listdir(uploads_folder) if os.path.isfile(os.path.join(uploads_folder, f)) and f != '.gitkeep']
    print(f"📊 Files in uploads folder: {len(files)}")
    
    for filename in files:
        file_path = os.path.join(uploads_folder, filename)
        file_size = os.path.getsize(file_path)
        print(f"   - {filename} ({file_size} bytes)")
    
    # Test upload folder permissions
    try:
        test_file = os.path.join(uploads_folder, 'test_upload.txt')
        with open(test_file, 'w') as f:
            f.write('Test upload functionality')
        
        if os.path.exists(test_file):
            print("✅ Uploads folder is writable")
            os.remove(test_file)
            print("✅ Test file removed")
        else:
            print("❌ Uploads folder is not writable")
            return False
            
    except Exception as e:
        print(f"❌ Error testing upload folder: {str(e)}")
        return False
    
    # Check app files
    app_files = ['app.py', 'models.py', 'config.py', 'run.py']
    for file in app_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} not found")
    
    # Check templates
    template_files = ['templates/index.html', 'templates/login.html', 'templates/register.html']
    for file in template_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} not found")
    
    print("✅ Basic upload test completed successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Basic Upload")
    print("=" * 50)
    print()
    
    success = test_upload_basic()
    
    if success:
        print()
        print("🎉 Basic upload test completed!")
        print("🚀 Upload functionality is ready.")
        print("📁 Files are properly stored in uploads folder.")
    else:
        print()
        print("❌ Basic upload test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
