#!/usr/bin/env python3
"""
Check uploads folder
"""

import os
import sys

def check_uploads():
    """Check uploads folder"""
    print("🔧 Checking uploads folder...")
    
    upload_folder = 'uploads'
    
    if not os.path.exists(upload_folder):
        print("❌ Uploads folder not found!")
        return False
    
    print(f"✅ Uploads folder exists: {upload_folder}")
    
    # List files
    files = os.listdir(upload_folder)
    print(f"📊 Files in uploads folder: {len(files)}")
    
    for filename in files:
        file_path = os.path.join(upload_folder, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            print(f"   - {filename} ({file_size} bytes)")
    
    # Test write permission
    try:
        test_file = os.path.join(upload_folder, 'test_write.txt')
        with open(test_file, 'w') as f:
            f.write('Test write permission')
        
        if os.path.exists(test_file):
            print("✅ Uploads folder is writable")
            os.remove(test_file)
            print("✅ Test file removed")
        else:
            print("❌ Uploads folder is not writable")
            return False
            
    except Exception as e:
        print(f"❌ Error testing write permission: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Check Uploads Folder")
    print("=" * 50)
    print()
    
    success = check_uploads()
    
    if success:
        print()
        print("🎉 Uploads folder is working correctly!")
    else:
        print()
        print("❌ Uploads folder has issues!")
    
    print()
    input("Press Enter to continue...")
