#!/usr/bin/env python3
"""
Ensure files from uploads folder are in database
"""

import os
import sys
import mimetypes
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File, User, Team

def ensure_files_in_database():
    """Ensure files from uploads folder are in database"""
    print("🔧 Ensuring files from uploads folder are in database...")
    
    with app.app_context():
        try:
            # Check current files in database
            current_files = File.query.all()
            print(f"📊 Current files in database: {len(current_files)}")
            
            # Get admin user
            admin_user = User.query.filter_by(username='frxadz').first()
            if not admin_user:
                print("❌ Admin user not found!")
                return False
            
            # Get team
            admin_team = admin_user.team
            if not admin_team:
                print("❌ Admin team not found!")
                return False
            
            # Check uploads folder
            uploads_folder = 'uploads'
            if not os.path.exists(uploads_folder):
                print("❌ Uploads folder not found!")
                return False
            
            # Get files from uploads folder
            files_in_folder = [f for f in os.listdir(uploads_folder) if os.path.isfile(os.path.join(uploads_folder, f)) and f != '.gitkeep']
            print(f"📁 Files in uploads folder: {len(files_in_folder)}")
            
            for filename in files_in_folder:
                print(f"   - {filename}")
            
            # Check if files are already in database
            stored_names = [f.stored_name for f in current_files]
            missing_files = []
            
            for filename in files_in_folder:
                if filename not in stored_names:
                    missing_files.append(filename)
                    print(f"❌ Missing from database: {filename}")
                else:
                    print(f"✅ Already in database: {filename}")
            
            # Add missing files to database
            if missing_files:
                print(f"\n🔧 Adding {len(missing_files)} missing files to database...")
                
                for filename in missing_files:
                    file_path = os.path.join(uploads_folder, filename)
                    
                    if os.path.exists(file_path):
                        file_size = os.path.getsize(file_path)
                        file_type = os.path.splitext(filename)[1][1:].lower() if '.' in filename else 'unknown'
                        mime_type = mimetypes.guess_type(file_path)[0]
                        
                        # Extract original name (remove UUID suffix)
                        original_name = filename
                        if '_' in filename and len(filename.split('_')[-1]) == 8:
                            name_parts = filename.rsplit('_', 1)
                            if len(name_parts) == 2:
                                original_name = name_parts[0] + os.path.splitext(name_parts[1])[0]
                        
                        # Generate download key
                        import secrets
                        download_key = secrets.token_urlsafe(24)
                        
                        # Create file record
                        file_record = File(
                            original_name=original_name,
                            stored_name=filename,
                            file_path=file_path,
                            file_size=file_size,
                            file_type=file_type,
                            mime_type=mime_type,
                            download_key=download_key,
                            owner_id=admin_user.id,
                            team_id=admin_team.id,
                            created_at=datetime.utcnow()
                        )
                        
                        db.session.add(file_record)
                        print(f"✅ Added to database: {original_name}")
                        print(f"   - Stored: {filename}")
                        print(f"   - Size: {file_size} bytes")
                        print(f"   - Type: {file_type}")
                        print(f"   - Key: {download_key[:8]}...")
                        print()
                
                # Commit changes
                db.session.commit()
                print("✅ All missing files added to database!")
            else:
                print("✅ All files already in database!")
            
            # Final check
            final_files = File.query.all()
            print(f"\n📊 Final files in database: {len(final_files)}")
            
            for f in final_files:
                print(f"   - {f.original_name} ({f.file_type}) - {f.format_file_size()}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
            db.session.rollback()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Ensure Files in Database")
    print("=" * 50)
    print()
    
    success = ensure_files_in_database()
    
    if success:
        print()
        print("🎉 Files are now in database!")
        print("🚀 Your files should appear in the application.")
    else:
        print()
        print("❌ Failed to ensure files in database!")
    
    print()
    input("Press Enter to continue...")
