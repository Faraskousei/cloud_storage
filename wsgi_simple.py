#!/usr/bin/env python3
"""
Simple WSGI entry point untuk Railway deployment
"""

import os
from app import app
from config import config

# Set production config untuk Railway
config_name = os.environ.get('FLASK_ENV', 'production')
if config_name not in config:
    config_name = 'production'

app.config.from_object(config[config_name])

# Pastikan folder uploads ada
upload_folder = app.config['UPLOAD_FOLDER']
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

# Simple database initialization
try:
    from models import db, init_database
    with app.app_context():
        init_database(app)
        print("✅ Database initialized successfully")
except Exception as e:
    print(f"⚠️  Database initialization warning: {str(e)}")

if __name__ == "__main__":
    app.run()
