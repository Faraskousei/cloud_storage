#!/usr/bin/env python3
"""
Test Railway configuration
"""

import os
import sys
from app import app
from config import config

def test_railway_config():
    """Test Railway configuration"""
    try:
        print("🔧 Testing Railway configuration...")
        
        # Set production config
        config_name = 'production'
        app.config.from_object(config[config_name])
        
        print(f"📊 Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        print(f"🌍 Environment: {config_name}")
        print(f"🔧 Debug mode: {app.config.get('DEBUG')}")
        
        # Check if DATABASE_URL is set
        database_url = os.environ.get('DATABASE_URL')
        if database_url:
            print(f"✅ DATABASE_URL found: {database_url[:50]}...")
        else:
            print("⚠️  DATABASE_URL not found, using fallback")
        
        # Test connection
        with app.app_context():
            from models import db, Team, User, File
            
            # Test database connection
            print("🔧 Testing database connection...")
            with db.engine.connect() as connection:
                connection.execute(db.text('SELECT 1'))
            print("✅ Database connection successful!")
            
            # Test queries
            teams = Team.query.all()
            users = User.query.all()
            files = File.query.all()
            
            print(f"✅ Teams: {len(teams)}")
            print(f"✅ Users: {len(users)}")
            print(f"✅ Files: {len(files)}")
            
            return True
            
    except Exception as e:
        print(f"❌ Railway configuration test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("  Railway Configuration Test")
    print("=" * 50)
    print()
    
    success = test_railway_config()
    
    if success:
        print("\n🎉 Railway configuration test passed!")
        print("🚀 Ready for Railway deployment!")
    else:
        print("\n❌ Railway configuration test failed!")
        print("🔧 Check your configuration and try again")
    
    print()
    print("=" * 50)
