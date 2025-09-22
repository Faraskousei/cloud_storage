#!/usr/bin/env python3
"""
Script untuk membuat file contoh dari tim yang berbeda untuk testing admin access
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, User, Team, File

def create_test_files():
    """Membuat file contoh untuk testing"""
    with app.app_context():
        try:
            print("🔍 Mencari teams yang tersedia...")
            teams = Team.query.all()
            print(f"📊 Ditemukan {len(teams)} teams:")
            for team in teams:
                print(f"   - {team.name} (ID: {team.id})")
            
            if len(teams) < 3:
                print("❌ Minimal 3 teams diperlukan!")
                return False
            
            # Buat file contoh untuk setiap tim
            test_files = [
                {
                    'name': 'Laporan KPPI.pdf',
                    'content': 'Ini adalah laporan dari tim KPPI',
                    'team_name': 'Tim KPPI'
                },
                {
                    'name': 'Dokumen SARPRAS.docx',
                    'content': 'Ini adalah dokumen dari tim SARPRAS',
                    'team_name': 'Tim Sarpras'
                },
                {
                    'name': 'Data PSDI.xlsx',
                    'content': 'Ini adalah data dari tim PSDI',
                    'team_name': 'Tim PSDI'
                }
            ]
            
            created_files = []
            
            for test_file in test_files:
                # Cari team
                team = Team.query.filter_by(name=test_file['team_name']).first()
                if not team:
                    print(f"❌ Team {test_file['team_name']} tidak ditemukan!")
                    continue
                
                # Buat file fisik
                upload_folder = 'uploads'
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)
                
                filename = f"test_{test_file['name']}"
                file_path = os.path.join(upload_folder, filename)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(test_file['content'])
                
                # Buat record di database
                file_record = File(
                    original_name=test_file['name'],
                    stored_name=filename,
                    file_path=file_path,
                    file_size=len(test_file['content']),
                    file_type=test_file['name'].split('.')[-1],
                    mime_type='text/plain',
                    description=f"File contoh dari {test_file['team_name']}",
                    team_id=team.id,
                    owner_id=1  # Admin user
                )
                
                db.session.add(file_record)
                created_files.append(test_file['name'])
            
            db.session.commit()
            
            print("✅ File contoh berhasil dibuat!")
            print("📁 File yang dibuat:")
            for file_name in created_files:
                print(f"   - {file_name}")
            
            print("\n🔐 Admin bisa melihat semua file ini:")
            print("   - Login sebagai admin atau frxadz")
            print("   - Lihat semua file dari semua tim")
            print("   - Download, view, dan hapus file dari tim manapun")
            
            return True
            
        except Exception as e:
            print(f"❌ Error saat membuat file contoh: {str(e)}")
            db.session.rollback()
            return False

if __name__ == '__main__':
    print("=" * 50)
    print("  Membuat File Contoh untuk Testing")
    print("=" * 50)
    print()
    
    success = create_test_files()
    
    if success:
        print()
        print("🚀 File contoh siap untuk testing!")
        print("🌐 Login di: http://localhost:5000/login")
        print("👤 Admin: admin/admin123 atau frxadz/admin")
    else:
        print()
        print("❌ Gagal membuat file contoh")
    
    print()
    print("=" * 50)
