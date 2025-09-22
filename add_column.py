#!/usr/bin/env python3
"""
Add download_code column to files table
"""

import sqlite3
import random

def add_download_code_column():
    """Add download_code column to files table"""
    print("🔧 Adding download_code column...")
    
    try:
        # Connect to database
        conn = sqlite3.connect('cloud_storage.db')
        cursor = conn.cursor()
        
        # Check if column exists
        cursor.execute("PRAGMA table_info(files)")
        columns = cursor.fetchall()
        column_names = [column[1] for column in columns]
        
        if 'download_code' in column_names:
            print("✅ download_code column already exists!")
            conn.close()
            return True
        
        # Add column
        cursor.execute("ALTER TABLE files ADD COLUMN download_code VARCHAR(6) NOT NULL DEFAULT '000000'")
        conn.commit()
        
        # Update existing files with random codes
        cursor.execute("SELECT id FROM files")
        files = cursor.fetchall()
        
        for file_id in files:
            # Generate random 6-digit code
            code = f"{random.randint(100000, 999999)}"
            cursor.execute("UPDATE files SET download_code = ? WHERE id = ?", (code, file_id[0]))
        
        conn.commit()
        conn.close()
        
        print(f"✅ Updated {len(files)} files with download codes")
        print("✅ download_code column added successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error adding column: {str(e)}")
        return False

if __name__ == "__main__":
    success = add_download_code_column()
    
    if success:
        print("🎉 Column added successfully!")
    else:
        print("❌ Failed to add column!")
    
    input("Press Enter to continue...")
