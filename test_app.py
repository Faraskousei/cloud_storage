#!/usr/bin/env python3
"""
Test script untuk memastikan aplikasi Flask berjalan dengan benar
"""

import sys
import os

# Tambahkan path aplikasi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app
    print("✅ Import app berhasil!")
    
    # Test konfigurasi Flask-Login
    from flask_login import LoginManager
    print("✅ Flask-Login tersedia!")
    
    # Test context processor
    with app.test_request_context():
        from flask import render_template_string
        template = "{{ current_user }}"
        result = render_template_string(template)
        print(f"✅ Context processor berfungsi: {result}")
    
    print("✅ Aplikasi siap dijalankan!")
    print("🌐 Akses di: http://localhost:5000")
    print("🔑 Login di: http://localhost:5000/login")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
