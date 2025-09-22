# 🚀 PythonAnywhere Deployment Guide

## 📋 Prerequisites
- PythonAnywhere account (free)
- All project files ready

## 🔧 Step 1: Create PythonAnywhere Account

### 1.1 Sign Up
1. **Go to PythonAnywhere:** https://pythonanywhere.com
2. **Sign up:** Create free account
3. **Verify Email:** Verify your email address
4. **Login:** Login to your account

### 1.2 Account Limits (Free)
- ✅ **1 Web App:** 1 web application
- ✅ **512 MB Storage:** 512 MB disk space
- ✅ **100 seconds CPU:** 100 seconds CPU per day
- ✅ **MySQL Database:** MySQL database included
- ✅ **Custom Domain:** pythonanywhere.com subdomain

## 🚀 Step 2: Upload Your Files

### 2.1 Upload Project Files
1. **Files Tab:** Go to "Files" tab
2. **Create Directory:** Create project directory
3. **Upload Files:** Upload all project files
4. **Extract:** Extract if needed

### 2.2 File Structure
```
/home/username/cloud-storage/
├── app.py
├── models.py
├── config.py
├── run.py
├── requirements.txt
├── templates/
├── static/
└── uploads/
```

## 🔧 Step 3: Install Dependencies

### 3.1 Install Python Packages
```bash
# Go to "Tasks" tab
# Create new task
pip3.10 install --user -r requirements.txt
```

### 3.2 Verify Installation
```bash
# Check if packages installed
pip3.10 list
```

## 🚀 Step 4: Database Setup

### 4.1 Create MySQL Database
1. **Databases Tab:** Go to "Databases" tab
2. **Create Database:** Click "Create database"
3. **Database Name:** cloud_storage
4. **Get Credentials:** Note down credentials

### 4.2 Import Database Schema
1. **Files Tab:** Go to "Files" tab
2. **Upload SQL:** Upload setup_database.sql
3. **MySQL Tab:** Go to "MySQL" tab
4. **Import:** Import setup_database.sql

### 4.3 Update Database Configuration
```python
# Update config.py for PythonAnywhere
class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'your-very-secret-key-here'
    MYSQL_HOST = 'username.mysql.pythonanywhere-services.com'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'username'
    MYSQL_PASSWORD = 'your-password'
    MYSQL_DATABASE = 'username$cloud_storage'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
```

## 🌐 Step 4: Create Web App

### 4.1 Create Web Application
1. **Web Tab:** Go to "Web" tab
2. **Add New Web App:** Click "Add a new web app"
3. **Flask:** Select Flask
4. **Python Version:** Select Python 3.10
5. **Source Code:** Set to your project directory

### 4.2 Configure WSGI
```python
# Update wsgi.py file
import sys
import os

# Add your project directory to Python path
path = '/home/username/cloud-storage'
if path not in sys.path:
    sys.path.append(path)

# Import your Flask app
from run import app as application

if __name__ == "__main__":
    application.run()
```

### 4.3 Set Environment Variables
```bash
# In Web tab, go to "Environment variables"
FLASK_ENV=production
SECRET_KEY=your-very-secret-key-here
```

## 🔧 Step 5: Configure Static Files

### 5.1 Static Files Configuration
1. **Web Tab:** Go to "Web" tab
2. **Static Files:** Configure static files
3. **URL:** /static/
4. **Directory:** /home/username/cloud-storage/static/

### 5.2 Media Files Configuration
1. **Web Tab:** Go to "Web" tab
2. **Static Files:** Configure media files
3. **URL:** /uploads/
4. **Directory:** /home/username/cloud-storage/uploads/

## 🌐 Step 6: Access Your App

### 6.1 Get Your URL
- **Web Tab:** Go to "Web" tab
- **Copy URL:** Copy your app URL
- **Example:** https://username.pythonanywhere.com

### 6.2 Test Your App
1. **Open URL:** Go to your PythonAnywhere URL
2. **Login:** Use admin/admin123 or frxadz/admin
3. **Upload Files:** Test file upload
4. **Test Features:** Test all features

## 🔧 Step 7: Custom Domain (Paid Feature)

### 7.1 Upgrade Account
1. **Account Tab:** Go to "Account" tab
2. **Upgrade:** Upgrade to paid plan
3. **Custom Domain:** Add your domain
4. **DNS Setup:** Point your domain to PythonAnywhere

### 7.2 SSL Certificate
- **Automatic:** PythonAnywhere provides free SSL
- **HTTPS:** Your app will be accessible via HTTPS

## 📊 Step 8: Monitoring

### 8.1 PythonAnywhere Dashboard
- **Logs:** View application logs
- **Metrics:** Monitor performance
- **Deployments:** Track deployments

### 8.2 Application Monitoring
- **Uptime:** Monitor app availability
- **Performance:** Track response times
- **Errors:** Monitor error rates

## 🚀 Step 9: Continuous Deployment

### 9.1 Manual Updates
1. **Files Tab:** Go to "Files" tab
2. **Upload New Files:** Upload updated files
3. **Reload Web App:** Reload your web app
4. **Test Changes:** Test your changes

### 9.2 Git Integration (Paid Feature)
```bash
# Install Git (paid feature)
git clone https://github.com/username/cloud-storage.git
cd cloud-storage
git pull origin main
```

## 🔧 Troubleshooting

### Common Issues
1. **Database Connection:** Check database credentials
2. **File Upload:** Check file permissions
3. **Static Files:** Check static file serving
4. **Environment Variables:** Check all variables

### Debug Commands
```bash
# Check logs in PythonAnywhere dashboard
# Check environment variables
# Check database connection
```

## 📱 Mobile Access

### Responsive Design
- ✅ **Bootstrap 5:** Mobile-friendly
- ✅ **Touch Support:** Touch-friendly buttons
- ✅ **Responsive Grid:** Adapts to screen size

### PWA Features
- ✅ **Offline Support:** Cache files
- ✅ **Install App:** Add to home screen
- ✅ **Push Notifications:** Push notifications

## 🔒 Security Best Practices

### 1. Environment Variables
```bash
# Never commit these to git
SECRET_KEY=your-very-secret-key
MYSQL_PASSWORD=your-database-password
FLASK_ENV=production
```

### 2. Database Security
- ✅ **Strong Passwords:** Use complex passwords
- ✅ **SSL Connection:** Use encrypted connections
- ✅ **Regular Backups:** Backup database regularly

### 3. Application Security
- ✅ **HTTPS Only:** Force HTTPS
- ✅ **Secure Headers:** Add security headers
- ✅ **Input Validation:** Validate all inputs

## 📞 Support

### Getting Help
- **PythonAnywhere Docs:** https://help.pythonanywhere.com
- **Community:** PythonAnywhere Community
- **Support:** PythonAnywhere Support

### Useful Commands
```bash
# Check Python version
python3.10 --version

# Check installed packages
pip3.10 list

# Check disk usage
df -h
```

---

**Happy Deploying! 🚀**
