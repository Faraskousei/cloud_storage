#!/usr/bin/env python3
"""
Create database with all required columns
"""

import os
import sys
from flask import Flask

def create_database():
    """Create database with all required columns"""
    print("🔧 Creating database with all required columns...")
    
    try:
        # Create Flask app
        app = Flask(__name__)
        
        # Load configuration
        config_name = os.environ.get('FLASK_ENV', 'development')
        if config_name == 'development':
            from config import DevelopmentConfig
            app.config.from_object(DevelopmentConfig)
        else:
            from config import ProductionConfig
            app.config.from_object(ProductionConfig)
        
        # Initialize database
        from models import db, init_database
        db.init_app(app)
        
        with app.app_context():
            # Drop all tables if they exist
            db.drop_all()
            
            # Create all tables
            db.create_all()
            
            # Initialize with default data
            init_database(app)
            
        print("✅ Database created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating database: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Create Database")
    print("=" * 50)
    print()
    
    success = create_database()
    
    if success:
        print()
        print("🎉 Database created successfully!")
        print("🔐 All tables and columns are ready!")
        print("📱 Download code feature is ready!")
    else:
        print()
        print("❌ Failed to create database!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
