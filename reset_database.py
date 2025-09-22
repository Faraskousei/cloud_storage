#!/usr/bin/env python3
"""
Script untuk reset database dengan download_key
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File, User, Team, init_database

def reset_database():
    """Reset database dengan download_key"""
    print("🔧 Resetting database with download_key...")
    
    with app.app_context():
        try:
            # Drop all tables
            print("🗑️ Dropping all tables...")
            db.drop_all()
            print("✅ All tables dropped")
            
            # Create all tables with new schema
            print("🔧 Creating new tables...")
            db.create_all()
            print("✅ New tables created")
            
            # Initialize database with default data
            print("🔧 Initializing database with default data...")
            init_database(app)
            print("✅ Database initialized")
            
            # Verify
            files_count = File.query.count()
            users_count = User.query.count()
            teams_count = Team.query.count()
            
            print(f"📊 Database stats:")
            print(f"   - Files: {files_count}")
            print(f"   - Users: {users_count}")
            print(f"   - Teams: {teams_count}")
            
            return True
            
        except Exception as e:
            print(f"❌ Reset failed: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Reset Database with Download Keys")
    print("=" * 50)
    print()
    
    success = reset_database()
    
    if success:
        print()
        print("🎉 Database reset completed successfully!")
        print("🚀 All tables now have download_key support.")
    else:
        print()
        print("❌ Reset failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
