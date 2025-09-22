#!/usr/bin/env python3
"""
Check files in database
"""

import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File

def check_database_files():
    """Check files in database"""
    print("🔧 Checking files in database...")
    
    with app.app_context():
        try:
            # Get all files
            files = File.query.all()
            print(f"📊 Total files in database: {len(files)}")
            
            if files:
                print("📁 Files in database:")
                for f in files:
                    print(f"   - {f.original_name}")
                    print(f"     Type: {f.file_type}")
                    print(f"     Size: {f.format_file_size()}")
                    print(f"     Stored: {f.stored_name}")
                    print(f"     Key: {f.download_key[:8]}...")
                    print()
            else:
                print("❌ No files found in database!")
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Check Database Files")
    print("=" * 50)
    print()
    
    check_database_files()
    
    print()
    input("Press Enter to continue...")
