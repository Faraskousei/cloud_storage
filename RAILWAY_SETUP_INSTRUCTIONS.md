
# 🚀 Railway Deployment Instructions

## 1. Setup Railway Account
- Go to https://railway.app
- Sign up with GitHub
- Create new project

## 2. Connect Repository
- Select "Deploy from GitHub repo"
- Choose your repository
- Railway will auto-detect Python

## 3. Add PostgreSQL Database
- Click "New" → "Database" → "PostgreSQL"
- Railway will create database
- Copy DATABASE_URL

## 4. Set Environment Variables
In Railway Dashboard → Variables, add:

FLASK_ENV=production
SECRET_KEY={secret_key}
DATABASE_URL=postgresql://postgres:password@host:port/railway
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=104857600
WTF_CSRF_ENABLED=true
SESSION_COOKIE_SECURE=true

## 5. Deploy
- Railway will auto-deploy from GitHub
- Check logs for deployment status
- Test application at Railway URL

## 6. Test Application
- Go to Railway URL
- Test login with admin/admin123
- Test register page
- Test file operations
- Test admin features

## 7. Monitor
- Check Railway Dashboard
- Monitor logs
- Check database metrics
- Monitor performance

## Troubleshooting
- Check Railway logs for errors
- Verify environment variables
- Test database connection
- Check application logs
