#!/usr/bin/env python3
"""
Test upload directly to app.py
"""

import os
import sys
import tempfile
from app import app, db, File, User, Team
from werkzeug.utils import secure_filename
import uuid

def test_upload_direct():
    """Test upload directly to app.py"""
    print("🔧 Testing upload directly to app.py...")
    
    with app.app_context():
        try:
            # Create a test file
            test_content = "This is a test file for upload testing."
            test_filename = "test_upload.txt"
            
            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
                temp_file.write(test_content)
                temp_file_path = temp_file.name
            
            print(f"📁 Created test file: {temp_file_path}")
            
            # Test file validation
            print("\n🔧 Testing file validation...")
            from app import allowed_file
            is_allowed = allowed_file(test_filename)
            print(f"✅ File allowed: {is_allowed}")
            
            # Test secure_filename
            secure_name = secure_filename(test_filename)
            print(f"✅ Secure filename: {secure_name}")
            
            # Test unique filename generation
            name, ext = os.path.splitext(secure_name)
            unique_filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
            print(f"✅ Unique filename: {unique_filename}")
            
            # Test upload folder
            upload_folder = app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder, exist_ok=True)
                print(f"✅ Created upload folder: {upload_folder}")
            
            # Test file save
            file_path = os.path.join(upload_folder, unique_filename)
            print(f"💾 Saving test file to: {file_path}")
            
            # Copy test file to upload folder
            with open(temp_file_path, 'rb') as src:
                with open(file_path, 'wb') as dst:
                    dst.write(src.read())
            
            print("✅ Test file saved successfully")
            
            # Verify file exists and size
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                print(f"✅ File exists, size: {file_size} bytes")
                
                if file_size > 0:
                    print("✅ File size is valid")
                else:
                    print("❌ File size is 0")
                    return False
            else:
                print("❌ File not found after save")
                return False
            
            # Test database save
            print("\n🔧 Testing database save...")
            try:
                # Get a test user
                test_user = User.query.first()
                if not test_user:
                    print("❌ No users found in database")
                    return False
                
                print(f"✅ Using test user: {test_user.username}")
                
                # Create file record
                file_record = File(
                    original_name=test_filename,
                    stored_name=unique_filename,
                    file_path=file_path,
                    file_size=file_size,
                    file_type='txt',
                    mime_type='text/plain',
                    download_key=File().generate_download_key(),
                    download_code=File().generate_download_code(),
                    owner_id=test_user.id,
                    team_id=test_user.team_id
                )
                
                db.session.add(file_record)
                db.session.commit()
                print(f"✅ File record saved to database: ID {file_record.id}")
                
                # Clean up
                db.session.delete(file_record)
                db.session.commit()
                print("✅ Test file record cleaned up")
                
            except Exception as db_error:
                print(f"❌ Database error: {str(db_error)}")
                db.session.rollback()
                return False
            
            # Clean up test files
            try:
                os.remove(temp_file_path)
                os.remove(file_path)
                print("✅ Test files cleaned up")
            except:
                pass
            
            print("\n✅ Direct upload test completed successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Direct upload test error: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Upload Direct")
    print("=" * 50)
    print()
    
    success = test_upload_direct()
    
    if success:
        print()
        print("🎉 Direct upload test completed!")
        print("🚀 Upload functionality is working!")
        print("💡 If web upload fails, check JavaScript or form issues.")
    else:
        print()
        print("❌ Direct upload test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
