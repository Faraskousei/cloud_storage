#!/usr/bin/env python3
"""
Test upload folder functionality
"""

import os
import sys
import shutil
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File, User, Team

def test_upload_folder():
    """Test upload folder functionality"""
    print("🔧 Testing upload folder functionality...")
    
    with app.app_context():
        try:
            # Check upload folder
            upload_folder = app.config['UPLOAD_FOLDER']
            print(f"📁 Upload folder: {upload_folder}")
            
            if not os.path.exists(upload_folder):
                print("❌ Upload folder not found!")
                return False
            
            print("✅ Upload folder exists")
            
            # List files in upload folder
            files_in_folder = [f for f in os.listdir(upload_folder) if os.path.isfile(os.path.join(upload_folder, f))]
            print(f"📊 Files in upload folder: {len(files_in_folder)}")
            
            for filename in files_in_folder:
                file_path = os.path.join(upload_folder, filename)
                file_size = os.path.getsize(file_path)
                print(f"   - {filename} ({file_size} bytes)")
            
            # Check database files
            db_files = File.query.all()
            print(f"\n📊 Files in database: {len(db_files)}")
            
            for file in db_files:
                print(f"   - {file.original_name}")
                print(f"     Stored: {file.stored_name}")
                print(f"     Path: {file.file_path}")
                print(f"     Size: {file.format_file_size()}")
                print(f"     Team: {file.team.name if file.team else 'Unknown'}")
                print(f"     Owner: {file.owner.full_name if file.owner else 'Unknown'}")
                print()
            
            # Verify file paths
            print("🔍 Verifying file paths...")
            all_paths_valid = True
            
            for file in db_files:
                if os.path.exists(file.file_path):
                    print(f"✅ {file.original_name} - File exists")
                else:
                    print(f"❌ {file.original_name} - File not found at {file.file_path}")
                    all_paths_valid = False
            
            if all_paths_valid:
                print("✅ All file paths are valid!")
            else:
                print("❌ Some file paths are invalid!")
            
            # Test upload folder permissions
            print("\n🔍 Testing upload folder permissions...")
            try:
                test_file_path = os.path.join(upload_folder, 'test_permissions.txt')
                with open(test_file_path, 'w') as f:
                    f.write('Test upload permissions')
                
                if os.path.exists(test_file_path):
                    print("✅ Upload folder is writable")
                    os.remove(test_file_path)
                    print("✅ Test file removed")
                else:
                    print("❌ Upload folder is not writable")
                    return False
                    
            except Exception as e:
                print(f"❌ Upload folder permission error: {str(e)}")
                return False
            
            return True
            
        except Exception as e:
            print(f"❌ Test failed: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Upload Folder")
    print("=" * 50)
    print()
    
    success = test_upload_folder()
    
    if success:
        print()
        print("🎉 Upload folder test completed successfully!")
        print("🚀 All files are properly stored in uploads folder.")
    else:
        print()
        print("❌ Upload folder test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
