#!/usr/bin/env python3
"""
Fix download_code column issue
"""

import os
import sys
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def fix_download_code_column():
    """Fix download_code column issue"""
    print("🔧 Fixing download_code column issue...")
    
    try:
        # Check if database exists
        db_path = 'cloud_storage.db'
        if not os.path.exists(db_path):
            print("❌ Database not found! Creating new database...")
            return create_new_database()
        
        print(f"✅ Database exists: {db_path}")
        
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if download_code column exists
        cursor.execute("PRAGMA table_info(files)")
        columns = cursor.fetchall()
        column_names = [column[1] for column in columns]
        
        if 'download_code' in column_names:
            print("✅ download_code column already exists!")
            conn.close()
            return True
        
        print("📝 Adding download_code column...")
        
        # Add download_code column
        cursor.execute("ALTER TABLE files ADD COLUMN download_code VARCHAR(6) NOT NULL DEFAULT '000000'")
        conn.commit()
        
        # Update existing files with random codes
        cursor.execute("SELECT id FROM files")
        files = cursor.fetchall()
        
        import random
        for file_id in files:
            # Generate random 6-digit code
            code = f"{random.randint(100000, 999999)}"
            cursor.execute("UPDATE files SET download_code = ? WHERE id = ?", (code, file_id[0]))
        
        conn.commit()
        conn.close()
        
        print(f"✅ Updated {len(files)} files with download codes")
        print("✅ download_code column added successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing download_code column: {str(e)}")
        return False

def create_new_database():
    """Create new database with all columns"""
    print("🔧 Creating new database...")
    
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
            # Create all tables
            db.create_all()
            init_database(app)
            
        print("✅ New database created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating new database: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Fix Download Code Column")
    print("=" * 50)
    print()
    
    success = fix_download_code_column()
    
    if success:
        print()
        print("🎉 Download code column fixed successfully!")
        print("🔐 All files now have download codes!")
        print("📱 Users need to enter code to download files!")
    else:
        print()
        print("❌ Failed to fix download code column!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
