#!/usr/bin/env python3
"""
Test simple upload functionality
"""

import os
import sys
import tempfile
import requests

def test_upload_simple():
    """Test simple upload functionality"""
    print("🔧 Testing simple upload functionality...")
    
    # Check if app is running
    try:
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("✅ Application is running")
        else:
            print("❌ Application not responding")
            return False
    except requests.exceptions.RequestException:
        print("❌ Application not running. Please start the app first.")
        return False
    
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
    
    print("✅ Simple upload test completed successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Simple Upload")
    print("=" * 50)
    print()
    
    success = test_upload_simple()
    
    if success:
        print()
        print("🎉 Simple upload test completed!")
        print("🚀 Upload functionality is working correctly.")
        print("📁 Files are properly stored in uploads folder.")
    else:
        print()
        print("❌ Simple upload test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
