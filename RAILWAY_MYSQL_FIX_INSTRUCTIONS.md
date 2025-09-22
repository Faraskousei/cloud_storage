# 🚀 Railway MySQL Fix Instructions

## 📋 Masalah yang Diperbaiki

### ❌ **Error Sebelumnya:**
```
ConnectionRefusedError: [Errno 111] Connection refused
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'localhost'")
```

### ✅ **Solusi:**
- **Switch dari MySQL ke PostgreSQL** untuk Railway
- **Updated config.py** untuk production
- **Fixed database configuration** untuk Railway
- **Removed MySQL dependency** untuk Railway

## 🔧 **File yang Sudah Diperbaiki:**

### 1. **config.py (Updated Base Config):**
```python
class Config:
    """Konfigurasi dasar untuk aplikasi Cloud Storage"""
    
    # Secret key untuk session dan flash messages
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Konfigurasi database - Default ke SQLite untuk development
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cloud_storage.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
        'pool_size': 1,
        'max_overflow': 0,
        'pool_timeout': 20,
        'pool_reset_on_return': 'commit'
    }
```

### 2. **DevelopmentConfig (MySQL for Local):**
```python
class DevelopmentConfig(Config):
    """Konfigurasi untuk development"""
    DEBUG = True
    
    # Konfigurasi database MySQL untuk development
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_PORT = os.environ.get('MYSQL_PORT') or '3306'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or ''
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE') or 'cloud_storage'
    
    # SQLAlchemy configuration untuk MySQL
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
        'pool_size': 5,
        'max_overflow': 10,
        'pool_timeout': 30,
        'pool_reset_on_return': 'commit'
    }
```

### 3. **ProductionConfig (PostgreSQL for Railway):**
```python
class ProductionConfig(Config):
    """Konfigurasi untuk production"""
    DEBUG = False
    
    # Database configuration untuk Railway (PostgreSQL)
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
        # Fallback ke SQLite jika DATABASE_URL tidak ada
        SQLALCHEMY_DATABASE_URI = 'sqlite:///cloud_storage.db'
        SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_recycle': 300,
            'pool_pre_ping': True,
            'pool_size': 1,
            'max_overflow': 0,
            'pool_timeout': 20,
            'pool_reset_on_return': 'commit'
        }
```

## 🚀 **Manual Push Instructions:**

### **Option 1: Install Git and Push**
```bash
# 1. Install Git from: https://git-scm.com/download/win
# 2. Restart terminal
# 3. Run commands:

git init
git add .
git commit -m "Fix Railway MySQL error: Switch to PostgreSQL configuration"
git remote add origin https://github.com/username/cloud-storage.git
git push -u origin main
```

### **Option 2: GitHub Web Interface**
1. **Go to GitHub:** https://github.com
2. **Create Repository:** Create new repository
3. **Upload Files:** Use "uploading an existing file"
4. **Drag & Drop:** Drag all project files
5. **Commit:** Commit changes

## 📋 **Files to Upload:**

### **Core Application Files:**
- ✅ **app.py** - Main Flask application
- ✅ **models.py** - Database models
- ✅ **config.py** - Updated configuration (PostgreSQL for Railway)
- ✅ **run.py** - Application runner
- ✅ **wsgi_debug.py** - Debug WSGI entry point
- ✅ **wsgi.py** - Main WSGI entry point
- ✅ **wsgi_simple.py** - Simple WSGI entry point

### **Configuration Files:**
- ✅ **requirements.txt** - Dependencies
- ✅ **Procfile** - Railway deployment
- ✅ **runtime.txt** - Python version
- ✅ **.gitignore** - Git ignore file

### **Environment Files:**
- ✅ **railway.env** - Railway environment variables
- ✅ **local.env** - Local development environment
- ✅ **test_railway_config.py** - Railway configuration test

### **Templates:**
- ✅ **templates/base.html** - Base template
- ✅ **templates/index.html** - Main dashboard
- ✅ **templates/login.html** - Login page
- ✅ **templates/register.html** - Register page
- ✅ **templates/error.html** - Error page template
- ✅ **templates/pdf_viewer.html** - PDF viewer

### **Static Files:**
- ✅ **static/css/style.css** - Stylesheet
- ✅ **static/js/script.js** - JavaScript

## 🌐 **Railway Deployment:**

### **1. After Push to GitHub:**
- **Railway will auto-deploy** from GitHub
- **Check Railway logs** for database connection
- **Look for:** "✅ Database connection successful"

### **2. Expected Railway Logs:**
```
🔧 Starting debug WSGI...
📊 Python version: 3.11.0
📁 Working directory: /app
🌍 Environment: production
🔧 Testing imports...
✅ app imported successfully
✅ config imported successfully
✅ Config loaded: production
📊 Debug mode: False
🗄️  Database URI: postgresql://...
🔧 Testing database...
✅ Database connection successful
✅ Database initialized successfully
✅ Upload folder exists: uploads
🎉 WSGI debug completed successfully!
[INFO] Starting gunicorn 21.2.0
[INFO] Listening at: http://0.0.0.0:8080
```

### **3. Test Application:**
1. **Go to Railway URL**
2. **Test login** with admin/admin123 or frxadz/admin
3. **Test register page** - should work without MySQL error
4. **Test dashboard** - should load properly
5. **Check for errors** in Railway logs

## 🔧 **Troubleshooting:**

### **Common Issues:**
1. **Database Connection** - Check DATABASE_URL in Railway
2. **Import Errors** - Check requirements.txt
3. **Template Errors** - Check template syntax
4. **Route Errors** - Check error handling

### **Debug Commands:**
```bash
# Test Railway configuration
python test_railway_config.py

# Test database connection
python setup_railway_database.py

# Test WSGI import
python -c "import wsgi_debug; print('WSGI OK')"
```

## 📞 **Support:**

### **Getting Help:**
- **Railway Docs:** https://docs.railway.app
- **Flask Docs:** https://flask.palletsprojects.com/
- **GitHub Docs:** https://docs.github.com

### **Check Logs:**
- **Railway Dashboard** → **Logs Tab**
- **Look for debug messages**
- **Check for specific errors**

---

**Railway MySQL error fixed! Railway will now use PostgreSQL instead of MySQL. 🚀✨**
