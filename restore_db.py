#!/usr/bin/env python3
"""
Database restore script untuk Railway PostgreSQL
"""

import os
import sys
import subprocess
from datetime import datetime
from app import app
from config import config

def get_railway_database_url():
    """Get Railway database URL"""
    try:
        # Set production config
        config_name = 'production'
        app.config.from_object(config[config_name])
        
        database_url = app.config.get('SQLALCHEMY_DATABASE_URI')
        if not database_url:
            print("❌ DATABASE_URL not found in configuration")
            return None
            
        print(f"📊 Database URI: {database_url[:50]}...")
        return database_url
        
    except Exception as e:
        print(f"❌ Error getting database URL: {str(e)}")
        return None

def restore_railway_database(dump_file):
    """Restore Railway PostgreSQL database from dump file"""
    try:
        print(f"🔧 Starting Railway database restore from: {dump_file}")
        
        # Check if dump file exists
        if not os.path.exists(dump_file):
            print(f"❌ Dump file not found: {dump_file}")
            return False
        
        # Get database URL
        database_url = get_railway_database_url()
        if not database_url:
            return False
        
        # Extract connection details from DATABASE_URL
        if database_url.startswith('postgresql://'):
            connection_string = database_url[13:]
            
            if '@' in connection_string:
                credentials, host_db = connection_string.split('@', 1)
                user, password = credentials.split(':', 1)
                
                if '/' in host_db:
                    host_port, database = host_db.split('/', 1)
                    host, port = host_port.split(':')
                    
                    print(f"🔧 Connection details:")
                    print(f"   Host: {host}")
                    print(f"   Port: {port}")
                    print(f"   Database: {database}")
                    print(f"   User: {user}")
                    
                    # Create psql command
                    cmd = [
                        'psql',
                        f'--host={host}',
                        f'--port={port}',
                        f'--username={user}',
                        f'--dbname={database}',
                        '--file={}'.format(dump_file)
                    ]
                    
                    # Set password via environment variable
                    env = os.environ.copy()
                    env['PGPASSWORD'] = password
                    
                    print("🔧 Running psql restore...")
                    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        print("✅ Database restore completed successfully!")
                        return True
                    else:
                        print(f"❌ psql restore failed: {result.stderr}")
                        return False
                else:
                    print("❌ Invalid database URL format")
                    return False
            else:
                print("❌ Invalid database URL format")
                return False
        else:
            print("❌ Not a PostgreSQL database URL")
            return False
            
    except Exception as e:
        print(f"❌ Database restore failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def list_dump_files():
    """List all dump files"""
    try:
        dump_dir = "database_dumps"
        if not os.path.exists(dump_dir):
            print("📁 No dump directory found")
            return []
        
        files = os.listdir(dump_dir)
        if not files:
            print("📁 No dump files found")
            return []
        
        print("📁 Available dump files:")
        dump_files = []
        for i, file in enumerate(sorted(files), 1):
            file_path = os.path.join(dump_dir, file)
            file_size = os.path.getsize(file_path)
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            print(f"   {i}. {file} ({file_size:,} bytes) - {file_time.strftime('%Y-%m-%d %H:%M:%S')}")
            dump_files.append(file_path)
        
        return dump_files
            
    except Exception as e:
        print(f"❌ Error listing dump files: {str(e)}")
        return []

def main():
    """Main function"""
    print("=" * 60)
    print("  Railway Database Restore Tool")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        dump_file = sys.argv[1]
        
        # Check if it's a number (selection from list)
        if dump_file.isdigit():
            dump_files = list_dump_files()
            if dump_files:
                try:
                    index = int(dump_file) - 1
                    if 0 <= index < len(dump_files):
                        dump_file = dump_files[index]
                        print(f"📁 Selected: {dump_file}")
                    else:
                        print("❌ Invalid selection")
                        return
                except ValueError:
                    print("❌ Invalid selection")
                    return
            else:
                print("❌ No dump files available")
                return
        else:
            # Check if file exists
            if not os.path.exists(dump_file):
                print(f"❌ File not found: {dump_file}")
                return
    else:
        # List available dump files
        dump_files = list_dump_files()
        if not dump_files:
            print("❌ No dump files available")
            return
        
        print("🔧 Please select a dump file to restore:")
        print("   Enter the number or file path")
        return
    
    # Confirm restore
    print(f"\n⚠️  WARNING: This will restore data to Railway database!")
    print(f"📁 Restore file: {dump_file}")
    confirm = input("   Are you sure? (yes/no): ").lower()
    
    if confirm != 'yes':
        print("❌ Restore cancelled")
        return
    
    # Restore database
    success = restore_railway_database(dump_file)
    
    if success:
        print("\n🎉 Database restore completed successfully!")
        print("🌐 Check your Railway application to verify the restore")
    else:
        print("\n❌ Database restore failed!")
        print("🔧 Check the error messages above")
    
    print()
    print("=" * 60)

if __name__ == '__main__':
    main()
