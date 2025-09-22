#!/usr/bin/env python3
"""
Test database connection untuk Railway
"""

import os
import sys
from app import app
from config import config

def test_database_connection():
    """Test database connection"""
    try:
        print("🔧 Testing database connection...")
        
        # Set production config
        config_name = os.environ.get('FLASK_ENV', 'production')
        app.config.from_object(config[config_name])
        
        print(f"📊 Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Test connection
        with app.app_context():
            from models import db, Team, User, File
            
            # Test database connection
            db.create_all()
            print("✅ Database connection successful!")
            
            # Test Team query
            teams = Team.query.all()
            print(f"✅ Teams query successful! Found {len(teams)} teams")
            
            # Test User query
            users = User.query.all()
            print(f"✅ Users query successful! Found {len(users)} users")
            
            # Test File query
            files = File.query.all()
            print(f"✅ Files query successful! Found {len(files)} files")
            
            return True
            
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("  Database Connection Test")
    print("=" * 50)
    print()
    
    success = test_database_connection()
    
    if success:
        print("\n🎉 Database connection test passed!")
        print("🚀 Your Railway deployment should work!")
    else:
        print("\n❌ Database connection test failed!")
        print("🔧 Check your DATABASE_URL and connection settings")
    
    print()
    print("=" * 50)
