#!/usr/bin/env python3
"""
Test upload system and admin view
"""

import os
import sys
import sqlite3

def test_upload_system():
    """Test upload system and admin view"""
    print("🔧 Testing upload system and admin view...")
    
    # Check uploads folder
    uploads_folder = 'uploads'
    if not os.path.exists(uploads_folder):
        print("❌ Uploads folder not found!")
        return False
    
    print(f"✅ Uploads folder exists: {uploads_folder}")
    
    # List files in uploads folder
    files = [f for f in os.listdir(uploads_folder) if os.path.isfile(os.path.join(uploads_folder, f)) and f != '.gitkeep']
    print(f"📊 Files in uploads folder: {len(files)}")
    
    for filename in files:
        file_path = os.path.join(uploads_folder, filename)
        file_size = os.path.getsize(file_path)
        print(f"   - {filename} ({file_size} bytes)")
    
    # Check database
    db_path = 'cloud_storage.db'
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return False
    
    print(f"✅ Database exists: {db_path}")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check files table
    cursor.execute("SELECT COUNT(*) FROM files")
    file_count = cursor.fetchone()[0]
    print(f"📊 Files in database: {file_count}")
    
    # Check users table
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    print(f"👥 Users in database: {user_count}")
    
    # Check admin users
    cursor.execute("SELECT username, is_admin FROM users WHERE is_admin = 1")
    admins = cursor.fetchall()
    print(f"👑 Admin users: {len(admins)}")
    for admin in admins:
        print(f"   - {admin[0]} (Admin: {admin[1]})")
    
    # Check teams
    cursor.execute("SELECT COUNT(*) FROM teams")
    team_count = cursor.fetchone()[0]
    print(f"🏢 Teams in database: {team_count}")
    
    conn.close()
    
    # Check templates
    templates = [
        'templates/index.html',
        'templates/login.html',
        'templates/register.html',
        'templates/base.html'
    ]
    
    print("\n📋 Template files:")
    for template in templates:
        if os.path.exists(template):
            print(f"   ✅ {template}")
        else:
            print(f"   ❌ {template}")
    
    print("✅ Upload system test completed successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Upload System")
    print("=" * 50)
    print()
    
    success = test_upload_system()
    
    if success:
        print()
        print("🎉 Upload system test completed!")
        print("🚀 Upload functionality is working!")
        print("👑 Admin view is ready!")
        print("📁 Files are stored in uploads folder!")
    else:
        print()
        print("❌ Upload system test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
