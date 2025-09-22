import os

class Config:
    """Konfigurasi dasar untuk aplikasi Cloud Storage"""
    
    # Secret key untuk session dan flash messages
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Konfigurasi database MySQL
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_PORT = os.environ.get('MYSQL_PORT') or '3306'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or ''
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE') or 'cloud_storage'
    
    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
        'pool_size': 5,
        'max_overflow': 10,
        'pool_timeout': 30,
        'pool_reset_on_return': 'commit'
    }
    
    # Konfigurasi upload
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB
    
    # Tipe file yang diizinkan
    ALLOWED_EXTENSIONS = {
        'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 
        'zip', 'rar', 'mp4', 'mp3', 'avi', 'mov'
    }
    
    # Login configuration
    LOGIN_DISABLED = False
    
    # Konfigurasi email (untuk notifikasi)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class DevelopmentConfig(Config):
    """Konfigurasi untuk development"""
    DEBUG = True

class ProductionConfig(Config):
    """Konfigurasi untuk production"""
    DEBUG = False
    
    # Pastikan secret key aman di production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database configuration untuk Railway (PostgreSQL)
    # Railway menyediakan DATABASE_URL untuk PostgreSQL
    if os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        # PostgreSQL connection pool settings
        SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_recycle': 300,
            'pool_pre_ping': True,
            'pool_size': 2,
            'max_overflow': 3,
            'pool_timeout': 20,
            'pool_reset_on_return': 'commit',
            'connect_args': {
                'connect_timeout': 10,
                'application_name': 'cloud_storage'
            }
        }
    else:
        # Fallback ke SQLite jika DATABASE_URL tidak ada (untuk testing)
        SQLALCHEMY_DATABASE_URI = 'sqlite:///cloud_storage.db'
        SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_recycle': 300,
            'pool_pre_ping': True,
            'pool_size': 1,
            'max_overflow': 0,
            'pool_timeout': 20,
            'pool_reset_on_return': 'commit'
        }

class TestingConfig(Config):
    """Konfigurasi untuk testing"""
    TESTING = True
    UPLOAD_FOLDER = 'test_uploads'

# Mapping konfigurasi
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
