#!/usr/bin/env python3
"""
Lazy database initialization untuk Railway
"""

import os
from flask import Flask
from models import db, init_database

def lazy_init_database(app):
    """Initialize database hanya jika diperlukan"""
    try:
        with app.app_context():
            # Check if tables exist
            from models import User, Team, File
            
            # Try to query one table to check if database is initialized
            Team.query.first()
            print("✅ Database already initialized")
            return True
    except Exception as e:
        print(f"🔄 Database not initialized, initializing now: {str(e)}")
        try:
            with app.app_context():
                init_database(app)
                print("✅ Database initialized successfully")
                return True
        except Exception as init_error:
            print(f"❌ Database initialization failed: {str(init_error)}")
            return False

def ensure_database_initialized(app):
    """Ensure database is initialized before first request"""
    if not hasattr(app, '_database_initialized'):
        app._database_initialized = lazy_init_database(app)
    return app._database_initialized
