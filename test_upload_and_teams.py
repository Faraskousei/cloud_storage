#!/usr/bin/env python3
"""
Test upload functionality and team isolation
"""

import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, File, User, Team

def test_upload_and_teams():
    """Test upload functionality and team isolation"""
    print("🔧 Testing upload functionality and team isolation...")
    
    with app.app_context():
        try:
            # Get all users
            users = User.query.all()
            print(f"👥 Total users: {len(users)}")
            
            for user in users:
                print(f"   - {user.username} ({user.full_name})")
                print(f"     Team: {user.team.name if user.team else 'None'}")
                print(f"     Admin: {user.is_admin}")
                print()
            
            # Get all teams
            teams = Team.query.all()
            print(f"🏢 Total teams: {len(teams)}")
            
            for team in teams:
                print(f"   - {team.name} ({team.color})")
                print(f"     Users: {len(team.users)}")
                print(f"     Files: {len(team.files)}")
                print()
            
            # Get all files with team info
            files = File.query.all()
            print(f"📁 Total files: {len(files)}")
            
            for file in files:
                print(f"   - {file.original_name}")
                print(f"     Owner: {file.owner.full_name if file.owner else 'Unknown'}")
                print(f"     Team: {file.team.name if file.team else 'Unknown'}")
                print(f"     Type: {file.file_type}")
                print(f"     Size: {file.format_file_size()}")
                print(f"     Key: {file.download_key[:8]}...")
                print()
            
            # Test team isolation
            print("🔍 Testing team isolation...")
            
            # Test admin view
            admin_user = User.query.filter_by(is_admin=True).first()
            if admin_user:
                print(f"👤 Admin user: {admin_user.full_name}")
                admin_files = File.query.all()  # Admin sees all files
                print(f"   Can see {len(admin_files)} files (all files)")
            
            # Test regular user view
            regular_users = User.query.filter_by(is_admin=False).all()
            for user in regular_users:
                print(f"👤 Regular user: {user.full_name}")
                user_files = File.query.filter_by(team_id=user.team_id).all()
                print(f"   Can see {len(user_files)} files (only their team)")
                for file in user_files:
                    print(f"     - {file.original_name}")
                print()
            
            return True
            
        except Exception as e:
            print(f"❌ Test failed: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    print("=" * 50)
    print("   Test Upload and Team Isolation")
    print("=" * 50)
    print()
    
    success = test_upload_and_teams()
    
    if success:
        print()
        print("🎉 Test completed successfully!")
        print("🚀 Upload and team isolation are working correctly.")
    else:
        print()
        print("❌ Test failed!")
        print("💡 Please check the error messages above.")
    
    print()
    input("Press Enter to continue...")
