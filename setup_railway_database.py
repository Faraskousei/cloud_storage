#!/usr/bin/env python3
"""
Setup database untuk Railway PostgreSQL
"""

import os
import sys
from app import app
from config import config

def setup_railway_database():
    """Setup database untuk Railway"""
    try:
        print("🔧 Setting up Railway database...")
        
        # Set production config
        config_name = os.environ.get('FLASK_ENV', 'production')
        app.config.from_object(config[config_name])
        
        print(f"📊 Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Test connection
        with app.app_context():
            from models import db, Team, User, File
            
            # Create all tables
            print("🔧 Creating database tables...")
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Check if teams exist
            teams = Team.query.all()
            if not teams:
                print("🔧 Creating default teams...")
                from models import init_database
                init_database(app)
                print("✅ Default teams and users created!")
            else:
                print(f"✅ Found {len(teams)} teams in database")
            
            # Test queries
            teams = Team.query.all()
            users = User.query.all()
            files = File.query.all()
            
            print(f"✅ Teams: {len(teams)}")
            print(f"✅ Users: {len(users)}")
            print(f"✅ Files: {len(files)}")
            
            return True
            
    except Exception as e:
        print(f"❌ Database setup failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("  Railway Database Setup")
    print("=" * 50)
    print()
    
    success = setup_railway_database()
    
    if success:
        print("\n🎉 Railway database setup completed!")
        print("🚀 Your Railway deployment should work now!")
    else:
        print("\n❌ Railway database setup failed!")
        print("🔧 Check your DATABASE_URL and connection settings")
    
    print()
    print("=" * 50)
