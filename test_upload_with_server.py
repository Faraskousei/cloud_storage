#!/usr/bin/env python3
"""
Test upload with running server
"""

import os
import sys
import tempfile
import requests
import time

def test_upload_with_server():
    """Test upload with running server"""
    print("🔧 Testing upload with running server...")
    
    # Check if server is running
    try:
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("✅ Server is running")
        else:
            print(f"❌ Server responded with status: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("❌ Server is not running. Please start the server first.")
        print("💡 Run: venv\\Scripts\\python.exe run.py")
        return False
    
    # Create test file
    test_content = "This is a test file for upload testing.\nLine 2\nLine 3"
    test_filename = "test_upload.txt"
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        temp_file.write(test_content)
        temp_file_path = temp_file.name
    
    print(f"📁 Created test file: {temp_file_path}")
    
    try:
        # Test upload
        print("📤 Testing file upload...")
        with open(temp_file_path, 'rb') as f:
            files = {'file': (test_filename, f, 'text/plain')}
            response = requests.post('http://localhost:5000/upload', files=files, timeout=30)
        
        print(f"📊 Upload response status: {response.status_code}")
        print(f"📊 Upload response: {response.text}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get('success'):
                    print("✅ Upload successful!")
                    print(f"📁 File: {data.get('message', 'Unknown')}")
                    return True
                else:
                    print(f"❌ Upload failed: {data.get('error', 'Unknown error')}")
                    return False
            except:
                print("❌ Invalid JSON response")
                return False
        else:
            print(f"❌ Upload failed with status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Upload test error: {str(e)}")
        return False
    
    finally:
        # Clean up
        try:
            os.remove(temp_file_path)
            print("✅ Test file cleaned up")
        except:
            pass

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Upload With Server")
    print("=" * 50)
    print()
    
    success = test_upload_with_server()
    
    if success:
        print()
        print("🎉 Upload test with server completed!")
        print("🚀 Upload functionality is working!")
    else:
        print()
        print("❌ Upload test with server failed!")
        print("💡 Please check server logs and try again.")
    
    print()
    input("Press Enter to continue...")
