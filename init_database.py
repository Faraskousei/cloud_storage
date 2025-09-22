#!/usr/bin/env python3
"""
Script untuk inisialisasi database MySQL
"""

import os
import sys
from app import app, db
from models import init_database

def main():
    """Inisialisasi database"""
    print("=" * 50)
    print("   Cloud Storage - Database Initialization")
    print("=" * 50)
    print()
    
    try:
        # Initialize database
        init_database(app)
        print("✅ Database berhasil diinisialisasi!")
        print()
        print("📊 Data yang dibuat:")
        print("   - 3 Teams: Development, Marketing, Operations")
        print("   - 1 Admin user: admin/admin123")
        print()
        print("🌐 Aplikasi siap dijalankan!")
        print("   Jalankan: python run.py")
        
    except Exception as e:
        print(f"❌ Error saat inisialisasi database: {e}")
        print()
        print("🔧 Pastikan:")
        print("   1. MySQL server sudah running")
        print("   2. Database 'cloud_storage' sudah dibuat")
        print("   3. Konfigurasi database sudah benar di config.py")
        sys.exit(1)

if __name__ == '__main__':
    main()
