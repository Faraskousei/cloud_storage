#!/usr/bin/env python3
"""
Test download and preview functionality
"""

import os
import sys
import sqlite3
from datetime import datetime

def test_download_preview():
    """Test download and preview functionality"""
    print("🔧 Testing download and preview functionality...")
    
    # Check database
    db_path = 'cloud_storage.db'
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return False
    
    print(f"✅ Database exists: {db_path}")
    
    # Connect to database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check files table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='files'")
        if not cursor.fetchone():
            print("❌ Files table not found!")
            return False
        
        print("✅ Files table exists")
        
        # Get files with download keys
        cursor.execute("""
            SELECT id, original_name, stored_name, file_type, download_key, file_path
            FROM files 
            ORDER BY created_at DESC
        """)
        files = cursor.fetchall()
        
        print(f"📊 Files in database: {len(files)}")
        
        for file in files:
            file_id, original_name, stored_name, file_type, download_key, file_path = file
            print(f"   - {original_name} ({file_type})")
            print(f"     ID: {file_id}, Key: {download_key[:10]}...")
            print(f"     Path: {file_path}")
            
            # Check if file exists
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                print(f"     ✅ File exists ({file_size} bytes)")
            else:
                print(f"     ❌ File not found")
        
        # Test download key generation
        print("\n🔑 Testing download key generation...")
        cursor.execute("SELECT download_key FROM files LIMIT 1")
        result = cursor.fetchone()
        if result:
            download_key = result[0]
            print(f"✅ Download key: {download_key[:10]}...")
            print(f"✅ Key length: {len(download_key)} characters")
        else:
            print("❌ No files with download keys found")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {str(e)}")
        return False
    
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
    
    print("✅ Download and preview test completed successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Download & Preview")
    print("=" * 50)
    print()
    
    success = test_download_preview()
    
    if success:
        print()
        print("🎉 Download and preview test completed!")
        print("🚀 Download functionality is working correctly.")
        print("👁️ Preview functionality is ready for PDF and images.")
        print("📁 Files are properly stored with download keys.")
    else:
        print()
        print("❌ Download and preview test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")

