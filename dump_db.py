#!/usr/bin/env python3
"""
Database dump script untuk Railway PostgreSQL
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

def dump_railway_database():
    """Dump Railway PostgreSQL database"""
    try:
        print("🔧 Starting Railway database dump...")
        
        # Get database URL
        database_url = get_railway_database_url()
        if not database_url:
            return False
        
        # Create dump directory
        dump_dir = "database_dumps"
        if not os.path.exists(dump_dir):
            os.makedirs(dump_dir)
            print(f"✅ Created dump directory: {dump_dir}")
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dump_file = f"{dump_dir}/railway_dump_{timestamp}.sql"
        
        print(f"📁 Dump file: {dump_file}")
        
        # Extract connection details from DATABASE_URL
        # Format: postgresql://user:password@host:port/database
        if database_url.startswith('postgresql://'):
            # Remove postgresql:// prefix
            connection_string = database_url[13:]
            
            # Split by @ to separate credentials from host
            if '@' in connection_string:
                credentials, host_db = connection_string.split('@', 1)
                user, password = credentials.split(':', 1)
                
                # Split host_db by / to separate host:port from database
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
                        f'--file={dump_file}'
                    ]
                    
                    # Set password via environment variable
                    env = os.environ.copy()
                    env['PGPASSWORD'] = password
                    
                    print("🔧 Running pg_dump...")
                    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        print("✅ Database dump completed successfully!")
                        print(f"📁 Dump saved to: {dump_file}")
                        
                        # Get file size
                        file_size = os.path.getsize(dump_file)
                        print(f"📊 Dump size: {file_size:,} bytes")
                        
                        return True
                    else:
                        print(f"❌ pg_dump failed: {result.stderr}")
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
        print(f"❌ Database dump failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def dump_railway_data_only():
    """Dump only data (no schema) from Railway database"""
    try:
        print("🔧 Starting Railway data-only dump...")
        
        # Get database URL
        database_url = get_railway_database_url()
        if not database_url:
            return False
        
        # Create dump directory
        dump_dir = "database_dumps"
        if not os.path.exists(dump_dir):
            os.makedirs(dump_dir)
            print(f"✅ Created dump directory: {dump_dir}")
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dump_file = f"{dump_dir}/railway_data_{timestamp}.sql"
        
        print(f"📁 Data dump file: {dump_file}")
        
        # Extract connection details from DATABASE_URL
        if database_url.startswith('postgresql://'):
            connection_string = database_url[13:]
            
            if '@' in connection_string:
                credentials, host_db = connection_string.split('@', 1)
                user, password = credentials.split(':', 1)
                
                if '/' in host_db:
                    host_port, database = host_db.split('/', 1)
                    host, port = host_port.split(':')
                    
                    # Create pg_dump command for data only
                    cmd = [
                        'pg_dump',
                        f'--host={host}',
                        f'--port={port}',
                        f'--username={user}',
                        f'--dbname={database}',
                        '--data-only',
                        '--verbose',
                        '--no-owner',
                        '--no-privileges',
                        f'--file={dump_file}'
                    ]
                    
                    # Set password via environment variable
                    env = os.environ.copy()
                    env['PGPASSWORD'] = password
                    
                    print("🔧 Running pg_dump (data only)...")
                    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        print("✅ Data dump completed successfully!")
                        print(f"📁 Data dump saved to: {dump_file}")
                        
                        # Get file size
                        file_size = os.path.getsize(dump_file)
                        print(f"📊 Data dump size: {file_size:,} bytes")
                        
                        return True
                    else:
                        print(f"❌ pg_dump failed: {result.stderr}")
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
        print(f"❌ Data dump failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def list_dump_files():
    """List all dump files"""
    try:
        dump_dir = "database_dumps"
        if not os.path.exists(dump_dir):
            print("📁 No dump directory found")
            return
        
        files = os.listdir(dump_dir)
        if not files:
            print("📁 No dump files found")
            return
        
        print("📁 Available dump files:")
        for file in sorted(files):
            file_path = os.path.join(dump_dir, file)
            file_size = os.path.getsize(file_path)
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            print(f"   {file} ({file_size:,} bytes) - {file_time.strftime('%Y-%m-%d %H:%M:%S')}")
            
    except Exception as e:
        print(f"❌ Error listing dump files: {str(e)}")

def main():
    """Main function"""
    print("=" * 60)
    print("  Railway Database Dump Tool")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'full':
            print("🔧 Full database dump (schema + data)")
            success = dump_railway_database()
        elif command == 'data':
            print("🔧 Data-only dump")
            success = dump_railway_data_only()
        elif command == 'list':
            list_dump_files()
            return
        else:
            print("❌ Unknown command. Use: full, data, or list")
            return
    else:
        print("🔧 Full database dump (schema + data)")
        success = dump_railway_database()
    
    if success:
        print("\n🎉 Database dump completed successfully!")
        print("📁 Check the database_dumps/ directory for dump files")
    else:
        print("\n❌ Database dump failed!")
        print("🔧 Make sure pg_dump is installed and Railway database is accessible")
    
    print()
    print("=" * 60)

if __name__ == '__main__':
    main()
