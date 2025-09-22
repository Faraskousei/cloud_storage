#!/usr/bin/env python3
"""
Simple script to restore files to database
"""

import os
import sys
import mimetypes
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File, User, Team

def simple_restore():
    """Simple restore files to database"""
    print("🔧 Restoring files to database...")
    
    with app.app_context():
        try:
            # Get admin user
            admin_user = User.query.filter_by(username='frxadz').first()
            if not admin_user:
                print("❌ Admin user not found!")
                return False
            
            print(f"👤 Found admin user: {admin_user.full_name}")
            
            # Get team
            admin_team = admin_user.team
            if not admin_team:
                print("❌ Admin team not found!")
                return False
            
            print(f"🏢 Found team: {admin_team.name}")
            
            # Files to restore
            files_to_restore = [
                {
                    'stored_name': 'MyReport_26-Aug-2025-faras_88f2d972.pdf',
                    'original_name': 'MyReport_26-Aug-2025-faras.pdf',
                    'file_type': 'pdf'
                },
                {
                    'stored_name': 'Screenshot_2025-09-22_093529_286fd2c8.png',
                    'original_name': 'Screenshot_2025-09-22_093529.png',
                    'file_type': 'png'
                }
            ]
            
            for file_info in files_to_restore:
                file_path = os.path.join('uploads', file_info['stored_name'])
                
                if os.path.exists(file_path):
                    file_size = os.path.getsize(file_path)
                    mime_type = mimetypes.guess_type(file_path)[0]
                    
                    # Generate download key
                    import secrets
                    download_key = secrets.token_urlsafe(24)
                    
                    # Create file record
                    file_record = File(
                        original_name=file_info['original_name'],
                        stored_name=file_info['stored_name'],
                        file_path=file_path,
                        file_size=file_size,
                        file_type=file_info['file_type'],
                        mime_type=mime_type,
                        download_key=download_key,
                        owner_id=admin_user.id,
                        team_id=admin_team.id,
                        created_at=datetime.utcnow()
                    )
                    
                    db.session.add(file_record)
                    print(f"✅ Added: {file_info['original_name']}")
                    print(f"   - Stored: {file_info['stored_name']}")
                    print(f"   - Size: {file_size} bytes")
                    print(f"   - Key: {download_key[:8]}...")
                    print()
                else:
                    print(f"❌ File not found: {file_path}")
            
            # Commit changes
            db.session.commit()
            print("✅ Files restored successfully!")
            
            # Check total files
            total_files = File.query.count()
            print(f"📊 Total files in database: {total_files}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
            db.session.rollback()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Simple Restore Files")
    print("=" * 50)
    print()
    
    success = simple_restore()
    
    if success:
        print()
        print("🎉 Files restored successfully!")
    else:
        print()
        print("❌ Restore failed!")
    
    print()
    input("Press Enter to continue...")
