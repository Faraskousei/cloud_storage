#!/usr/bin/env python3
"""
Debug upload issues in app.py
"""

import os
import sys
import traceback

def debug_upload_issues():
    """Debug upload issues in app.py"""
    print("🔧 Debugging upload issues in app.py...")
    
    try:
        # Test imports
        print("📦 Testing imports...")
        from app import app, db, File, User, Team
        from werkzeug.utils import secure_filename
        import uuid
        import mimetypes
        print("✅ All imports successful")
        
        # Test app configuration
        print("\n🔧 Testing app configuration...")
        with app.app_context():
            print(f"✅ Upload folder: {app.config.get('UPLOAD_FOLDER', 'NOT SET')}")
            print(f"✅ Allowed extensions: {app.config.get('ALLOWED_EXTENSIONS', 'NOT SET')}")
            print(f"✅ Max content length: {app.config.get('MAX_CONTENT_LENGTH', 'NOT SET')}")
            print(f"✅ Debug mode: {app.config.get('DEBUG', 'NOT SET')}")
        
        # Test database connection
        print("\n🔧 Testing database connection...")
        with app.app_context():
            try:
                # Test database query
                user_count = User.query.count()
                team_count = Team.query.count()
                file_count = File.query.count()
                print(f"✅ Database connection OK")
                print(f"   Users: {user_count}")
                print(f"   Teams: {team_count}")
                print(f"   Files: {file_count}")
            except Exception as db_error:
                print(f"❌ Database error: {str(db_error)}")
                return False
        
        # Test upload folder
        print("\n🔧 Testing upload folder...")
        upload_folder = app.config.get('UPLOAD_FOLDER', 'uploads')
        if not os.path.exists(upload_folder):
            print(f"❌ Upload folder not found: {upload_folder}")
            try:
                os.makedirs(upload_folder, exist_ok=True)
                print(f"✅ Created upload folder: {upload_folder}")
            except Exception as e:
                print(f"❌ Cannot create upload folder: {str(e)}")
                return False
        else:
            print(f"✅ Upload folder exists: {upload_folder}")
        
        # Test folder permissions
        try:
            test_file = os.path.join(upload_folder, 'test_write.tmp')
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            print("✅ Upload folder is writable")
        except Exception as e:
            print(f"❌ Upload folder not writable: {str(e)}")
            return False
        
        # Test File model methods
        print("\n🔧 Testing File model methods...")
        try:
            # Test generate_download_key
            test_file = File()
            download_key = test_file.generate_download_key()
            print(f"✅ generate_download_key: {download_key}")
            
            # Test generate_download_code
            download_code = test_file.generate_download_code()
            print(f"✅ generate_download_code: {download_code}")
            
        except Exception as e:
            print(f"❌ File model methods error: {str(e)}")
            return False
        
        # Test allowed_file function
        print("\n🔧 Testing allowed_file function...")
        try:
            from app import allowed_file
            test_files = ['test.pdf', 'test.txt', 'test.exe', 'test.jpg']
            for test_file in test_files:
                is_allowed = allowed_file(test_file)
                print(f"   {test_file}: {'✅' if is_allowed else '❌'}")
        except Exception as e:
            print(f"❌ allowed_file function error: {str(e)}")
            return False
        
        print("\n✅ All upload components are working!")
        return True
        
    except Exception as e:
        print(f"❌ Debug error: {str(e)}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Debug Upload Issues")
    print("=" * 50)
    print()
    
    success = debug_upload_issues()
    
    if success:
        print()
        print("🎉 Upload debug completed!")
        print("🚀 All components are working!")
        print("💡 If upload still fails, check browser console and server logs.")
    else:
        print()
        print("❌ Upload debug found issues!")
        print("💡 Please fix the errors above.")
    
    print()
    input("Press Enter to continue...")
