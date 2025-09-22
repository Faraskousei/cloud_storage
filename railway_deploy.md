# 🚀 Railway Deployment Guide

## 📋 Prerequisites
- GitHub account
- Railway account (free)
- Git installed

## 🔧 Step 1: Prepare Repository

### 1.1 Create GitHub Repository
```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit"

# Create GitHub repository and push
git remote add origin https://github.com/username/cloud-storage.git
git branch -M main
git push -u origin main
```

### 1.2 Update Files for Production
```bash
# Copy production requirements
cp requirements_production.txt requirements.txt

# Update config.py to include production config
# Add ProductionConfig to config.py
```

## 🚀 Step 2: Deploy to Railway

### 2.1 Connect to Railway
1. **Go to Railway:** https://railway.app
2. **Sign up/Login:** Use GitHub account
3. **New Project:** Click "New Project"
4. **Deploy from GitHub:** Select your repository

### 2.2 Configure Environment Variables
```bash
# In Railway Dashboard, go to Variables tab
FLASK_ENV=production
SECRET_KEY=your-very-secret-key-here
DATABASE_URL=postgresql://user:pass@host:port/dbname
```

### 2.3 Database Setup
1. **Add PostgreSQL:** Click "Add Database" → PostgreSQL
2. **Get Connection String:** Copy DATABASE_URL
3. **Set Environment Variable:** Add DATABASE_URL to variables

## 🔧 Step 3: Configure Application

### 3.1 Update run.py for Production
```python
import os
from app import app
from config import config

if __name__ == '__main__':
    config_name = os.environ.get('FLASK_ENV', 'production')
    app.config.from_object(config[config_name])
    
    # Initialize database
    from models import db, init_database
    with app.app_context():
        init_database(app)
    
    print("🚀 Cloud Storage Server started!")
    print("🌐 Access your app at: https://your-app.railway.app")
    
    app.run(
        debug=False,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000))
    )
```

### 3.2 Update config.py
```python
# Add to config.py
class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 🌐 Step 4: Access Your App

### 4.1 Get Your URL
- **Railway Dashboard:** Go to your project
- **Copy URL:** Copy the generated URL
- **Example:** https://your-app-name.railway.app

### 4.2 Test Your App
1. **Open URL:** Go to your Railway URL
2. **Login:** Use admin/admin123 or frxadz/admin
3. **Upload Files:** Test file upload
4. **Test Features:** Test all features

## 🔧 Step 5: Custom Domain (Optional)

### 5.1 Add Custom Domain
1. **Railway Dashboard:** Go to your project
2. **Settings:** Click "Settings"
3. **Custom Domain:** Add your domain
4. **DNS Setup:** Point your domain to Railway

### 5.2 SSL Certificate
- **Automatic:** Railway provides free SSL
- **HTTPS:** Your app will be accessible via HTTPS

## 📊 Step 6: Monitoring

### 6.1 Railway Dashboard
- **Logs:** View application logs
- **Metrics:** Monitor performance
- **Deployments:** Track deployments

### 6.2 Application Monitoring
- **Uptime:** Monitor app availability
- **Performance:** Track response times
- **Errors:** Monitor error rates

## 🚀 Step 7: Continuous Deployment

### 7.1 Auto-Deploy
- **GitHub Integration:** Push to GitHub auto-deploys
- **Branch Protection:** Protect main branch
- **Review Process:** Review changes before deploy

### 7.2 Manual Deploy
```bash
# Update your code
git add .
git commit -m "Update app"
git push origin main

# Railway will auto-deploy
```

## 🔧 Troubleshooting

### Common Issues
1. **Database Connection:** Check DATABASE_URL
2. **File Upload:** Check file permissions
3. **Static Files:** Check static file serving
4. **Environment Variables:** Check all variables

### Debug Commands
```bash
# Check logs in Railway dashboard
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
DATABASE_URL=your-database-url
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
- **Railway Docs:** https://docs.railway.app
- **Community:** Railway Discord
- **Support:** Railway Support

### Useful Commands
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Deploy to Railway
railway deploy
```

---

**Happy Deploying! 🚀**
