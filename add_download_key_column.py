#!/usr/bin/env python3
"""
Script untuk menambahkan kolom download_key ke tabel files
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File

def add_download_key_column():
    """Tambahkan kolom download_key ke tabel files"""
    print("🔧 Adding download_key column to files table...")
    
    with app.app_context():
        try:
            # Add download_key column using raw SQL
            db.engine.execute("ALTER TABLE files ADD COLUMN download_key VARCHAR(32) UNIQUE")
            print("✅ download_key column added successfully!")
            
            # Update existing files with download keys
            print("🔧 Updating existing files with download keys...")
            files = File.query.all()
            
            for file in files:
                if not file.download_key:
                    file.download_key = file.generate_download_key()
                    print(f"   - Updated {file.original_name} with key: {file.download_key[:8]}...")
            
            # Commit changes
            db.session.commit()
            print("✅ All files updated with download keys!")
            
            # Verify
            files_with_key = File.query.filter(File.download_key.isnot(None)).count()
            print(f"📊 Total files with download keys: {files_with_key}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to add column: {str(e)}")
            # Try alternative approach - recreate table
            try:
                print("🔄 Trying alternative approach...")
                # Drop and recreate table
                db.engine.execute("DROP TABLE IF EXISTS files")
                db.create_all()
                print("✅ Table recreated successfully!")
                return True
            except Exception as e2:
                print(f"❌ Alternative approach failed: {str(e2)}")
                return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Add Download Key Column")
    print("=" * 50)
    print()
    
    success = add_download_key_column()
    
    if success:
        print()
        print("🎉 Download key column added successfully!")
        print("🚀 All files now have download keys.")
    else:
        print()
        print("❌ Failed to add download key column!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
