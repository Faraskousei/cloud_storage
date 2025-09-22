#!/usr/bin/env python3
"""
Script untuk update file yang sudah ada dengan download_key
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File

def update_existing_files():
    """Update file yang sudah ada dengan download_key"""
    print("🔧 Updating existing files with download keys...")
    
    with app.app_context():
        try:
            # Get all files without download_key
            files_without_key = File.query.filter(File.download_key.is_(None)).all()
            
            if not files_without_key:
                print("✅ All files already have download keys!")
                return True
            
            print(f"📁 Found {len(files_without_key)} files without download keys")
            
            # Update each file with download_key
            for file in files_without_key:
                # Generate new download key
                file.download_key = file.generate_download_key()
                print(f"   - Updated {file.original_name} with key: {file.download_key[:8]}...")
            
            # Commit changes
            db.session.commit()
            print("✅ All files updated successfully!")
            
            # Verify update
            files_with_key = File.query.filter(File.download_key.isnot(None)).count()
            print(f"📊 Total files with download keys: {files_with_key}")
            
            return True
            
        except Exception as e:
            print(f"❌ Update failed: {str(e)}")
            db.session.rollback()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Update Existing Files with Download Keys")
    print("=" * 50)
    print()
    
    success = update_existing_files()
    
    if success:
        print()
        print("🎉 Files updated successfully!")
        print("🚀 Download links are now available for all files.")
    else:
        print()
        print("❌ Update failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
