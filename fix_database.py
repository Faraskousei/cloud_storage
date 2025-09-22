#!/usr/bin/env python3
"""
Script untuk memperbaiki database dan mengatasi error upload_time
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, User, Team, File, init_database

def fix_database():
    """Perbaiki database dan pastikan semua tabel ada"""
    print("🔧 Starting database fix...")
    
    with app.app_context():
        try:
            # Create all tables
            print("📊 Creating database tables...")
            db.create_all()
            print("✅ Database tables created successfully")
            
            # Initialize database with default data
            print("🔧 Initializing database with default data...")
            init_database(app)
            print("✅ Database initialized successfully")
            
            # Check if we have any files
            files_count = File.query.count()
            print(f"📁 Found {files_count} files in database")
            
            # Check if we have any users
            users_count = User.query.count()
            print(f"👥 Found {users_count} users in database")
            
            # Check if we have any teams
            teams_count = Team.query.count()
            print(f"🏢 Found {teams_count} teams in database")
            
            # Test file query
            print("🧪 Testing file query...")
            files = File.query.all()
            for file in files:
                print(f"   - File: {file.original_name}")
                print(f"     Created: {file.created_at}")
                print(f"     Size: {file.format_file_size()}")
                print(f"     Type: {file.file_type}")
                if hasattr(file, 'team') and file.team:
                    print(f"     Team: {file.team.name}")
                print()
            
            print("✅ Database fix completed successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Database fix failed: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Database Fix Script")
    print("=" * 50)
    print()
    
    success = fix_database()
    
    if success:
        print()
        print("🎉 Database fix completed successfully!")
        print("🚀 You can now run the application without errors.")
    else:
        print()
        print("❌ Database fix failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
