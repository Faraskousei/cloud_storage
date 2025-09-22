#!/usr/bin/env python3
"""
WSGI entry point untuk Railway deployment
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

# Lazy database initialization
from lazy_db_init import ensure_database_initialized

@app.before_first_request
def initialize_database():
    """Initialize database before first request"""
    ensure_database_initialized(app)

if __name__ == "__main__":
    app.run()
