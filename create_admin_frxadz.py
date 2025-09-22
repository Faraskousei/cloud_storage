#!/usr/bin/env python3
"""
Script sederhana untuk membuat user admin frxadz
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, User, Team

def create_admin_frxadz():
    """Membuat user admin frxadz"""
    with app.app_context():
        try:
            print("🔍 Mencari team yang tersedia...")
            teams = Team.query.all()
            print(f"📊 Ditemukan {len(teams)} teams:")
            for team in teams:
                print(f"   - {team.name} (ID: {team.id})")
            
            if not teams:
                print("❌ Tidak ada team yang ditemukan!")
                return False
            
            # Gunakan team pertama yang tersedia
            admin_team = teams[0]
            print(f"✅ Menggunakan team: {admin_team.name}")
            
            # Check if user already exists
            existing_user = User.query.filter_by(username='frxadz').first()
            if existing_user:
                print("⚠️  User 'frxadz' sudah ada dalam database!")
                print(f"📧 Email: {existing_user.email}")
                print(f"👤 Full Name: {existing_user.full_name}")
                print(f"🔑 Is Admin: {existing_user.is_admin}")
                print(f"👥 Team: {existing_user.get_team_name()}")
                return True
            
            # Create new admin user
            frxadz_user = User(
                username='frxadz',
                email='frxadz@company.com',
                full_name='Frxadz Administrator',
                team_id=admin_team.id,
                is_admin=True,
                is_active=True
            )
            frxadz_user.set_password('admin')
            
            # Add to database
            db.session.add(frxadz_user)
            db.session.commit()
            
            print("✅ User admin berhasil ditambahkan!")
            print("📧 Username: frxadz")
            print("🔑 Password: admin")
            print("👤 Full Name: Frxadz Administrator")
            print("👥 Team: " + admin_team.name)
            print("🔐 Role: Administrator")
            print("✅ Status: Active")
            
            return True
            
        except Exception as e:
            print(f"❌ Error saat menambahkan user: {str(e)}")
            db.session.rollback()
            return False

if __name__ == '__main__':
    print("=" * 50)
    print("  Membuat User Admin Frxadz")
    print("=" * 50)
    print()
    
    success = create_admin_frxadz()
    
    if success:
        print()
        print("🚀 User admin siap digunakan!")
        print("🌐 Login di: http://localhost:5000/login")
        print("👤 Username: frxadz")
        print("🔑 Password: admin")
    else:
        print()
        print("❌ Gagal menambahkan user admin")
    
    print()
    print("=" * 50)
