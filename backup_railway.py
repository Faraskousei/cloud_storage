#!/usr/bin/env python3
"""
Backup script untuk Railway PostgreSQL database
"""

import os
import sys
import subprocess
import json
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

def backup_railway_database():
    """Backup Railway PostgreSQL database"""
    try:
        print("🔧 Starting Railway database backup...")
        
        # Get database URL
        database_url = get_railway_database_url()
        if not database_url:
            return False
        
        # Create backup directory
        backup_dir = "railway_backups"
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            print(f"✅ Created backup directory: {backup_dir}")
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{backup_dir}/railway_backup_{timestamp}.sql"
        
        print(f"📁 Backup file: {backup_file}")
        
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
                    
                    # Create pg_dump command
                    cmd = [
                        'pg_dump',
                        f'--host={host}',
                        f'--port={port}',
                        f'--username={user}',
                        f'--dbname={database}',
                        '--verbose',
                        '--clean',
                        '--no-owner',
                        '--no-privileges',
                        '--format=plain',
                        f'--file={backup_file}'
                    ]
                    
                    # Set password via environment variable
                    env = os.environ.copy()
                    env['PGPASSWORD'] = password
                    
                    print("🔧 Running pg_dump backup...")
                    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        print("✅ Database backup completed successfully!")
                        print(f"📁 Backup saved to: {backup_file}")
                        
                        # Get file size
                        file_size = os.path.getsize(backup_file)
                        print(f"📊 Backup size: {file_size:,} bytes")
                        
                        # Create backup info file
                        info_file = f"{backup_dir}/backup_info_{timestamp}.json"
                        backup_info = {
                            'timestamp': timestamp,
                            'backup_file': backup_file,
                            'file_size': file_size,
                            'database_url': database_url[:50] + "...",
                            'host': host,
                            'port': port,
                            'database': database,
                            'user': user
                        }
                        
                        with open(info_file, 'w') as f:
                            json.dump(backup_info, f, indent=2)
                        
                        print(f"📋 Backup info saved to: {info_file}")
                        
                        return True
                    else:
                        print(f"❌ pg_dump backup failed: {result.stderr}")
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
        print(f"❌ Database backup failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def list_backup_files():
    """List all backup files"""
    try:
        backup_dir = "railway_backups"
        if not os.path.exists(backup_dir):
            print("📁 No backup directory found")
            return
        
        files = os.listdir(backup_dir)
        if not files:
            print("📁 No backup files found")
            return
        
        print("📁 Available backup files:")
        for file in sorted(files):
            if file.endswith('.sql'):
                file_path = os.path.join(backup_dir, file)
                file_size = os.path.getsize(file_path)
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                print(f"   {file} ({file_size:,} bytes) - {file_time.strftime('%Y-%m-%d %H:%M:%S')}")
            
    except Exception as e:
        print(f"❌ Error listing backup files: {str(e)}")

def cleanup_old_backups(days=30):
    """Clean up old backup files"""
    try:
        backup_dir = "railway_backups"
        if not os.path.exists(backup_dir):
            print("📁 No backup directory found")
            return
        
        files = os.listdir(backup_dir)
        if not files:
            print("📁 No backup files found")
            return
        
        from datetime import timedelta
        cutoff_date = datetime.now() - timedelta(days=days)
        
        cleaned_count = 0
        for file in files:
            if file.endswith('.sql'):
                file_path = os.path.join(backup_dir, file)
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                if file_time < cutoff_date:
                    os.remove(file_path)
                    cleaned_count += 1
                    print(f"🗑️  Removed old backup: {file}")
        
        if cleaned_count > 0:
            print(f"✅ Cleaned up {cleaned_count} old backup files")
        else:
            print("✅ No old backup files to clean up")
            
    except Exception as e:
        print(f"❌ Error cleaning up old backups: {str(e)}")

def main():
    """Main function"""
    print("=" * 60)
    print("  Railway Database Backup Tool")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'backup':
            print("🔧 Creating Railway database backup")
            success = backup_railway_database()
        elif command == 'list':
            list_backup_files()
            return
        elif command == 'cleanup':
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
            print(f"🔧 Cleaning up backups older than {days} days")
            cleanup_old_backups(days)
            return
        else:
            print("❌ Unknown command. Use: backup, list, or cleanup")
            return
    else:
        print("🔧 Creating Railway database backup")
        success = backup_railway_database()
    
    if success:
        print("\n🎉 Database backup completed successfully!")
        print("📁 Check the railway_backups/ directory for backup files")
    else:
        print("\n❌ Database backup failed!")
        print("🔧 Make sure pg_dump is installed and Railway database is accessible")
    
    print()
    print("=" * 60)

if __name__ == '__main__':
    main()
