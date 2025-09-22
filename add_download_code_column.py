#!/usr/bin/env python3
"""
Add download_code column to files table
"""

import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, File

def add_download_code_column():
    """Add download_code column to files table"""
    print("🔧 Adding download_code column to files table...")
    
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
        db.init_app(app)
        
        with app.app_context():
            # Check if column already exists
            try:
                # Try to query download_code column
                db.session.execute("SELECT download_code FROM files LIMIT 1")
                print("✅ download_code column already exists!")
                return True
            except Exception:
                # Column doesn't exist, add it
                print("📝 Adding download_code column...")
                
                # Add column
                db.session.execute("ALTER TABLE files ADD COLUMN download_code VARCHAR(6) NOT NULL DEFAULT '000000'")
                db.session.commit()
                
                # Update existing files with random codes
                files = File.query.all()
                for file in files:
                    if not file.download_code or file.download_code == '000000':
                        file.download_code = file.generate_download_code()
                        db.session.add(file)
                
                db.session.commit()
                
                print(f"✅ Updated {len(files)} files with download codes")
                print("✅ download_code column added successfully!")
                return True
                
    except Exception as e:
        print(f"❌ Error adding download_code column: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Add Download Code Column")
    print("=" * 50)
    print()
    
    success = add_download_code_column()
    
    if success:
        print()
        print("🎉 Download code column added successfully!")
        print("🔐 All files now have download codes!")
        print("📱 Users need to enter code to download files!")
    else:
        print()
        print("❌ Failed to add download code column!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
