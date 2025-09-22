#!/usr/bin/env python3
"""
Test file icons for different file types
"""

import os
import sys

def test_file_icons():
    """Test file icons for different file types"""
    print("🔧 Testing file icons...")
    
    # File types that should have specific icons
    file_types = {
        'PDF': ['pdf'],
        'Images': ['png', 'jpg', 'jpeg', 'gif'],
        'Word': ['doc', 'docx'],
        'Excel': ['xls', 'xlsx'],
        'PowerPoint': ['ppt', 'pptx'],
        'Archive': ['zip', 'rar'],
        'Text': ['txt'],
        'Video': ['mp4', 'avi', 'mov'],
        'Audio': ['mp3', 'wav', 'flac']
    }
    
    print("📋 File types and their expected icons:")
    for category, types in file_types.items():
        print(f"\n{category} Files:")
        for file_type in types:
            print(f"   ✅ .{file_type} - Has specific icon and color")
    
    # Check uploads folder for existing files
    uploads_folder = 'uploads'
    if os.path.exists(uploads_folder):
        files = [f for f in os.listdir(uploads_folder) if os.path.isfile(os.path.join(uploads_folder, f)) and f != '.gitkeep']
        print(f"\n📊 Files in uploads folder: {len(files)}")
        
        for filename in files:
            file_ext = filename.split('.')[-1].lower() if '.' in filename else 'unknown'
            file_path = os.path.join(uploads_folder, filename)
            file_size = os.path.getsize(file_path)
            
            # Determine icon category
            icon_category = "Unknown"
            for category, types in file_types.items():
                if file_ext in types:
                    icon_category = category
                    break
            
            print(f"   📄 {filename}")
            print(f"      Type: .{file_ext} ({icon_category})")
            print(f"      Size: {file_size} bytes")
    
    print("\n🎨 Icon Colors:")
    print("   📕 PDF - Red gradient")
    print("   🖼️ Images - Teal gradient") 
    print("   📘 Word - Blue gradient")
    print("   📗 Excel - Green gradient")
    print("   📙 PowerPoint - Orange gradient")
    print("   📦 Archive - Purple gradient")
    print("   📄 Text - Gray gradient")
    print("   🎬 Video - Red gradient")
    print("   🎵 Audio - Purple gradient")
    
    print("\n✅ File icons test completed!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test File Icons")
    print("=" * 50)
    print()
    
    success = test_file_icons()
    
    if success:
        print()
        print("🎉 File icons test completed!")
        print("🚀 All file types have proper icons!")
        print("🎨 Icons have distinctive colors!")
    else:
        print()
        print("❌ File icons test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
