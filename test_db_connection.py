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
        # Set production config
        config_name = os.environ.get('FLASK_ENV', 'production')
        app.config.from_object(config[config_name])
        
        print("🔧 Testing database connection...")
        print(f"📊 Database URL: {app.config['SQLALCHEMY_DATABASE_URI']}")
        print(f"🔧 Engine Options: {app.config['SQLALCHEMY_ENGINE_OPTIONS']}")
        
        # Test connection
        with app.app_context():
            from models import db
            db.create_all()
            print("✅ Database connection successful!")
            print("✅ Tables created successfully!")
            
            # Test query
            from models import Team
            teams = Team.query.all()
            print(f"✅ Query successful! Found {len(teams)} teams")
            
            return True
            
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
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
