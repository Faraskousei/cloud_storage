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

# Initialize database
from models import db, init_database
with app.app_context():
    init_database(app)

if __name__ == "__main__":
    app.run()
