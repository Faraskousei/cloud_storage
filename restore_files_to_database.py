#!/usr/bin/env python3
"""
Script untuk mengembalikan file yang ada di folder uploads ke database
"""

import os
import sys
import mimetypes
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File, User, Team

def restore_files_to_database():
    """Restore files from uploads folder to database"""
    print("🔧 Restoring files from uploads folder to database...")
    
    with app.app_context():
        try:
            # Get uploads folder path
            uploads_folder = app.config['UPLOAD_FOLDER']
            print(f"📁 Checking uploads folder: {uploads_folder}")
            
            # Get all files in uploads folder
            if not os.path.exists(uploads_folder):
                print("❌ Uploads folder not found!")
                return False
            
            files_in_folder = os.listdir(uploads_folder)
            print(f"📊 Found {len(files_in_folder)} files in uploads folder")
            
            # Get admin user (for file ownership)
            admin_user = User.query.filter_by(username='frxadz').first()
            if not admin_user:
                print("❌ Admin user not found!")
                return False
            
            # Get team (for file team assignment)
            admin_team = admin_user.team
            if not admin_team:
                print("❌ Admin team not found!")
                return False
            
            print(f"👤 Using admin user: {admin_user.full_name}")
            print(f"🏢 Using team: {admin_team.name}")
            
            restored_count = 0
            
            for filename in files_in_folder:
                if os.path.isfile(os.path.join(uploads_folder, filename)):
                    file_path = os.path.join(uploads_folder, filename)
                    
                    # Get file info
                    file_size = os.path.getsize(file_path)
                    file_type = os.path.splitext(filename)[1][1:].lower() if '.' in filename else 'unknown'
                    mime_type = mimetypes.guess_type(file_path)[0]
                    
                    # Extract original name (remove UUID suffix)
                    original_name = filename
                    if '_' in filename and len(filename.split('_')[-1]) == 8:
                        # Remove UUID suffix
                        name_parts = filename.rsplit('_', 1)
                        if len(name_parts) == 2:
                            original_name = name_parts[0] + os.path.splitext(name_parts[1])[0]
                    
                    # Create file record
                    file_record = File(
                        original_name=original_name,
                        stored_name=filename,
                        file_path=file_path,
                        file_size=file_size,
                        file_type=file_type,
                        mime_type=mime_type,
                        download_key=File().generate_download_key(),
                        owner_id=admin_user.id,
                        team_id=admin_team.id,
                        created_at=datetime.utcnow()
                    )
                    
                    db.session.add(file_record)
                    restored_count += 1
                    
                    print(f"   ✅ Restored: {original_name}")
                    print(f"      - Stored: {filename}")
                    print(f"      - Size: {file_record.format_file_size()}")
                    print(f"      - Type: {file_type}")
                    print(f"      - Key: {file_record.download_key[:8]}...")
                    print()
            
            # Commit changes
            db.session.commit()
            print(f"✅ Successfully restored {restored_count} files to database!")
            
            # Verify
            total_files = File.query.count()
            print(f"📊 Total files in database: {total_files}")
            
            return True
            
        except Exception as e:
            print(f"❌ Restore failed: {str(e)}")
            import traceback
            traceback.print_exc()
            db.session.rollback()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Restore Files to Database")
    print("=" * 50)
    print()
    
    success = restore_files_to_database()
    
    if success:
        print()
        print("🎉 Files restored successfully!")
        print("🚀 All files from uploads folder are now in database.")
    else:
        print()
        print("❌ Restore failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
