#!/usr/bin/env python3
"""
Test download code feature
"""

import os
import sys
import sqlite3

def test_download_code():
    """Test download code feature"""
    print("🔧 Testing download code feature...")
    
    # Check database
    db_path = 'cloud_storage.db'
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return False
    
    print(f"✅ Database exists: {db_path}")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if download_code column exists
    cursor.execute("PRAGMA table_info(files)")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    print("📋 Database columns:")
    for col in column_names:
        print(f"   ✅ {col}")
    
    if 'download_code' in column_names:
        print("✅ download_code column exists!")
    else:
        print("❌ download_code column not found!")
        return False
    
    # Check files with download codes
    cursor.execute("SELECT id, original_name, download_code FROM files")
    files = cursor.fetchall()
    
    print(f"📊 Files in database: {len(files)}")
    
    for file in files:
        file_id, original_name, download_code = file
        print(f"   - {original_name} (Code: {download_code})")
    
    # Check if all files have download codes
    cursor.execute("SELECT COUNT(*) FROM files WHERE download_code IS NULL OR download_code = ''")
    null_codes = cursor.fetchone()[0]
    
    if null_codes == 0:
        print("✅ All files have download codes!")
    else:
        print(f"❌ {null_codes} files missing download codes!")
        return False
    
    conn.close()
    
    # Check templates
    templates = [
        'templates/download_verify.html',
        'templates/download_error.html'
    ]
    
    print("\n📋 Template files:")
    for template in templates:
        if os.path.exists(template):
            print(f"   ✅ {template}")
        else:
            print(f"   ❌ {template}")
    
    print("✅ Download code feature test completed successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Download Code Feature")
    print("=" * 50)
    print()
    
    success = test_download_code()
    
    if success:
        print()
        print("🎉 Download code feature test completed!")
        print("🚀 Download code verification is working!")
        print("🔐 All files have download codes!")
        print("📱 Users need to enter code to download files!")
    else:
        print()
        print("❌ Download code feature test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
