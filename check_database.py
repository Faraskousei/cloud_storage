#!/usr/bin/env python3
"""
Check database structure
"""

import sqlite3
import os

def check_database():
    """Check database structure"""
    print("🔧 Checking database structure...")
    
    db_path = 'cloud_storage.db'
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        return False
    
    print(f"✅ Database exists: {db_path}")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    
    print("📋 Tables in database:")
    for table in table_names:
        print(f"   ✅ {table}")
    
    if 'files' in table_names:
        print("\n📋 Files table columns:")
        cursor.execute("PRAGMA table_info(files)")
        columns = cursor.fetchall()
        for col in columns:
            print(f"   ✅ {col[1]} ({col[2]})")
    
    conn.close()
    return True

if __name__ == "__main__":
    check_database()
    input("Press Enter to continue...")
