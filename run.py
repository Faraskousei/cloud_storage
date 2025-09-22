#!/usr/bin/env python3
"""
File untuk menjalankan aplikasi Cloud Storage
"""

import os
from app import app
from config import config

if __name__ == '__main__':
    # Ambil konfigurasi dari environment variable
    config_name = os.environ.get('FLASK_ENV', 'development')
    
    # Pastikan menggunakan development config untuk local development
    if config_name not in config:
        config_name = 'development'
        print(f"⚠️  Konfigurasi '{os.environ.get('FLASK_ENV')}' tidak ditemukan, menggunakan 'development'")
    
    app.config.from_object(config[config_name])
    print(f"✅ Menggunakan konfigurasi: {config_name}")
    
    # Pastikan folder uploads ada
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
        print(f"✅ Folder {upload_folder} berhasil dibuat")
    
    # Jalankan aplikasi
    print("🚀 Cloud Storage Server dimulai...")
    print("📁 Upload folder:", os.path.abspath(upload_folder))
    print("🌐 Akses aplikasi di: http://localhost:5000")
    print("⏹️  Tekan Ctrl+C untuk menghentikan server")
    print("-" * 50)
    
    app.run(
        debug=app.config['DEBUG'],
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000))
    )
