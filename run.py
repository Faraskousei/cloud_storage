#!/usr/bin/env python3
"""
File untuk menjalankan aplikasi Cloud Storage
"""

import os
import sys
from app import app, db, init_database
from config import config

def ensure_upload_folder():
    """Pastikan folder uploads ada dan dapat ditulis"""
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        try:
            os.makedirs(upload_folder, exist_ok=True)
            print(f"✅ Folder {upload_folder} berhasil dibuat")
        except Exception as e:
            print(f"❌ Error membuat folder {upload_folder}: {str(e)}")
            return False
    
    # Test write permission
    try:
        test_file = os.path.join(upload_folder, 'test_write.tmp')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        print(f"✅ Folder {upload_folder} dapat ditulis")
    except Exception as e:
        print(f"❌ Error menulis ke folder {upload_folder}: {str(e)}")
        return False
    
    return True

if __name__ == '__main__':
    try:
        # Ambil konfigurasi dari environment variable
        config_name = os.environ.get('FLASK_ENV', 'development')
        
        # Pastikan menggunakan development config untuk local development
        if config_name not in config:
            config_name = 'development'
            print(f"⚠️  Konfigurasi '{os.environ.get('FLASK_ENV')}' tidak ditemukan, menggunakan 'development'")
        
        app.config.from_object(config[config_name])
        print(f"✅ Menggunakan konfigurasi: {config_name}")
        
        # Inisialisasi database
        with app.app_context():
            db.create_all()
            init_database(app)
            print("✅ Database initialized")
        
        # Pastikan folder uploads ada dan dapat ditulis
        if not ensure_upload_folder():
            print("❌ Upload folder tidak dapat dibuat atau ditulis!")
            sys.exit(1)
        
        # Jalankan aplikasi
        print("🚀 Cloud Storage Server dimulai...")
        print("📁 Upload folder:", os.path.abspath(app.config['UPLOAD_FOLDER']))
        print("🌐 Akses aplikasi di: http://localhost:5000")
        print("⏹️  Tekan Ctrl+C untuk menghentikan server")
        print("-" * 50)
        
        app.run(
            debug=app.config['DEBUG'],
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000)),
            threaded=True
        )
        
    except Exception as e:
        print(f"❌ Error starting server: {str(e)}")
        sys.exit(1)
