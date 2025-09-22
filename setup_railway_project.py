#!/usr/bin/env python3
"""
Setup Railway project dengan database PostgreSQL
"""

import os
import sys
import secrets
from app import app
from config import config

def generate_secret_key():
    """Generate secure secret key"""
    return secrets.token_hex(32)

def setup_railway_project():
    """Setup Railway project configuration"""
    try:
        print("🔧 Setting up Railway project...")
        
        # Generate secret key
        secret_key = generate_secret_key()
        print(f"🔑 Generated SECRET_KEY: {secret_key}")
        
        # Set production config
        config_name = 'production'
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
        print(f"❌ Railway project setup failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def create_railway_instructions():
    """Create Railway deployment instructions"""
    instructions = """
# 🚀 Railway Deployment Instructions

## 1. Setup Railway Account
- Go to https://railway.app
- Sign up with GitHub
- Create new project

## 2. Connect Repository
- Select "Deploy from GitHub repo"
- Choose your repository
- Railway will auto-detect Python

## 3. Add PostgreSQL Database
- Click "New" → "Database" → "PostgreSQL"
- Railway will create database
- Copy DATABASE_URL

## 4. Set Environment Variables
In Railway Dashboard → Variables, add:

FLASK_ENV=production
SECRET_KEY={secret_key}
DATABASE_URL=postgresql://postgres:password@host:port/railway
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=104857600
WTF_CSRF_ENABLED=true
SESSION_COOKIE_SECURE=true

## 5. Deploy
- Railway will auto-deploy from GitHub
- Check logs for deployment status
- Test application at Railway URL

## 6. Test Application
- Go to Railway URL
- Test login with admin/admin123
- Test register page
- Test file operations
- Test admin features

## 7. Monitor
- Check Railway Dashboard
- Monitor logs
- Check database metrics
- Monitor performance

## Troubleshooting
- Check Railway logs for errors
- Verify environment variables
- Test database connection
- Check application logs
"""
    
    with open('RAILWAY_SETUP_INSTRUCTIONS.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("📋 Created RAILWAY_SETUP_INSTRUCTIONS.md")

if __name__ == '__main__':
    print("=" * 60)
    print("  Railway Project Setup")
    print("=" * 60)
    print()
    
    success = setup_railway_project()
    
    if success:
        print("\n🎉 Railway project setup completed!")
        print("🚀 Ready for Railway deployment!")
        
        # Create instructions
        create_railway_instructions()
        print("📋 Check RAILWAY_SETUP_INSTRUCTIONS.md for deployment steps")
    else:
        print("\n❌ Railway project setup failed!")
        print("🔧 Check your configuration and try again")
    
    print()
    print("=" * 60)
