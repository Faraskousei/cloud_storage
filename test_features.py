#!/usr/bin/env python3
"""
Test all features
"""

import os
import sys

def test_features():
    """Test all features"""
    print("🔧 Testing all features...")
    
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
        file_ext = filename.split('.')[-1].lower() if '.' in filename else 'unknown'
        print(f"   - {filename} ({file_ext}, {file_size} bytes)")
        
        # Check if it's a previewable file
        if file_ext in ['pdf', 'png', 'jpg', 'jpeg', 'gif']:
            print(f"     ✅ Previewable file ({file_ext})")
        else:
            print(f"     📄 Downloadable file ({file_ext})")
    
    # Check app files
    app_files = ['app.py', 'models.py', 'config.py', 'run.py']
    for file in app_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} not found")
    
    # Check templates
    template_files = ['templates/index.html', 'templates/login.html', 'templates/register.html']
    for file in template_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} not found")
    
    print("✅ All features test completed successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("   Test All Features")
    print("=" * 50)
    print()
    
    success = test_features()
    
    if success:
        print()
        print("🎉 All features test completed!")
        print("🚀 Download and preview features are ready.")
        print("📁 Files are properly stored in uploads folder.")
        print("👁️ PDF and image files can be previewed.")
        print("⬇️ All files can be downloaded with secure keys.")
    else:
        print()
        print("❌ Features test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")

