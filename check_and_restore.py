#!/usr/bin/env python3
"""
Simple script to check and restore files
"""

import os
import sys
import mimetypes
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def check_files():
    """Check files in uploads folder"""
    print("🔧 Checking files in uploads folder...")
    
    uploads_folder = 'uploads'
    
    if not os.path.exists(uploads_folder):
        print("❌ Uploads folder not found!")
        return
    
    files = os.listdir(uploads_folder)
    print(f"📊 Found {len(files)} files in uploads folder:")
    
    for filename in files:
        file_path = os.path.join(uploads_folder, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            file_type = os.path.splitext(filename)[1][1:].lower() if '.' in filename else 'unknown'
            print(f"   - {filename}")
            print(f"     Size: {file_size} bytes")
            print(f"     Type: {file_type}")
            print()

if __name__ == "__main__":
    print("=" * 50)
    print("   Check Files in Uploads Folder")
    print("=" * 50)
    print()
    
    check_files()
    
    print()
    input("Press Enter to continue...")
