#!/usr/bin/env python3
"""
Debug WSGI entry point untuk Railway deployment
"""

import os
import sys
import traceback

def debug_startup():
    """Debug startup process"""
    print("🔧 Starting debug WSGI...")
    print(f"📊 Python version: {sys.version}")
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"🌍 Environment: {os.environ.get('FLASK_ENV', 'production')}")
    
    try:
        # Test imports
        print("🔧 Testing imports...")
        from app import app
        print("✅ app imported successfully")
        
        from config import config
        print("✅ config imported successfully")
        
        # Test config
        config_name = os.environ.get('FLASK_ENV', 'production')
        if config_name not in config:
            config_name = 'production'
            print(f"⚠️  Using fallback config: {config_name}")
        
        app.config.from_object(config[config_name])
        print(f"✅ Config loaded: {config_name}")
        print(f"📊 Debug mode: {app.config.get('DEBUG')}")
        print(f"🗄️  Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
        
        # Test database
        print("🔧 Testing database...")
        try:
            from models import db, init_database
            with app.app_context():
                init_database(app)
                print("✅ Database initialized successfully")
        except Exception as db_error:
            print(f"⚠️  Database warning: {str(db_error)}")
            print("🔄 Continuing without database init...")
        
        # Test upload folder
        upload_folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            print(f"✅ Created upload folder: {upload_folder}")
        else:
            print(f"✅ Upload folder exists: {upload_folder}")
        
        print("🎉 WSGI debug completed successfully!")
        return app
        
    except Exception as e:
        print(f"❌ WSGI debug failed: {str(e)}")
        print("📋 Traceback:")
        traceback.print_exc()
        return None

# Initialize app with debug
app = debug_startup()

if app is None:
    print("❌ Failed to initialize app")
    sys.exit(1)

if __name__ == "__main__":
    app.run()
