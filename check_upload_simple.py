#!/usr/bin/env python3
"""
Check simple upload functionality
"""

import os
import sys

def check_upload_simple():
    """Check simple upload functionality"""
    print("🔧 Checking simple upload functionality...")
    
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
    
    print("✅ Simple upload check completed successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Check Simple Upload")
    print("=" * 50)
    print()
    
    success = check_upload_simple()
    
    if success:
        print()
        print("🎉 Simple upload check completed!")
        print("🚀 Upload functionality is ready.")
        print("📁 Files are properly stored in uploads folder.")
    else:
        print()
        print("❌ Simple upload check failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
