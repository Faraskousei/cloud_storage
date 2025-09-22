@echo off
echo ========================================
echo   Update Procfile for Railway
echo ========================================
echo.

echo 🔧 Updating Procfile...
echo.

echo 📝 Current Procfile:
type Procfile

echo.
echo 🔄 Updating to simple WSGI...
echo web: gunicorn wsgi_simple:app > Procfile

echo 📝 New Procfile:
type Procfile

echo.
echo 📦 Adding changes...
git add .

echo 💾 Committing changes...
git commit -m "Update Procfile: Use wsgi_simple for better compatibility"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully updated Procfile!
echo.
echo 🚀 Railway deployment should work now!
echo.
echo 📋 Changes made:
echo    - Updated Procfile to use wsgi_simple
echo    - Better compatibility with Railway
echo    - Simpler WSGI entry point
echo.
echo 🌐 Your app will be accessible at Railway URL!
echo.
pause
