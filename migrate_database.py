#!/usr/bin/env python3
"""
Script untuk migrate database dengan download_key
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File, User, Team

def migrate_database():
    """Migrate database dengan download_key"""
    print("🔧 Migrating database with download_key...")
    
    with app.app_context():
        try:
            # Backup existing data
            print("📦 Backing up existing data...")
            existing_files = []
            for file in File.query.all():
                existing_files.append({
                    'original_name': file.original_name,
                    'stored_name': file.stored_name,
                    'file_path': file.file_path,
                    'file_size': file.file_size,
                    'file_type': file.file_type,
                    'mime_type': file.mime_type,
                    'description': file.description,
                    'is_public': file.is_public,
                    'owner_id': file.owner_id,
                    'team_id': file.team_id,
                    'created_at': file.created_at,
                    'updated_at': file.updated_at
                })
            
            print(f"📁 Found {len(existing_files)} files to migrate")
            
            # Drop and recreate files table
            print("🔄 Recreating files table...")
            File.__table__.drop(db.engine, checkfirst=True)
            db.create_all()
            
            # Restore data with download_key
            print("📥 Restoring data with download keys...")
            for file_data in existing_files:
                # Generate download key
                import secrets
                download_key = secrets.token_urlsafe(24)
                
                new_file = File(
                    original_name=file_data['original_name'],
                    stored_name=file_data['stored_name'],
                    file_path=file_data['file_path'],
                    file_size=file_data['file_size'],
                    file_type=file_data['file_type'],
                    mime_type=file_data['mime_type'],
                    description=file_data['description'],
                    is_public=file_data['is_public'],
                    download_key=download_key,
                    owner_id=file_data['owner_id'],
                    team_id=file_data['team_id'],
                    created_at=file_data['created_at'],
                    updated_at=file_data['updated_at']
                )
                
                db.session.add(new_file)
                print(f"   - Migrated {file_data['original_name']} with key: {download_key[:8]}...")
            
            # Commit changes
            db.session.commit()
            print("✅ Database migration completed successfully!")
            
            # Verify
            files_count = File.query.count()
            print(f"📊 Total files after migration: {files_count}")
            
            return True
            
        except Exception as e:
            print(f"❌ Migration failed: {str(e)}")
            import traceback
            traceback.print_exc()
            db.session.rollback()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Database Migration with Download Keys")
    print("=" * 50)
    print()
    
    success = migrate_database()
    
    if success:
        print()
        print("🎉 Database migration completed successfully!")
        print("🚀 All files now have download keys.")
    else:
        print()
        print("❌ Migration failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
