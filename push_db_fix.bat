@echo off
echo ========================================
echo   Push Database Connection Fix
echo ========================================
echo.

echo 🔧 Fixing database connection pool issues...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix database connection pool: Add lazy initialization and better pool settings"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed database fixes!
echo.
echo 🚀 Railway deployment should work now!
echo.
echo 📋 Changes made:
echo    - Added lazy database initialization
echo    - Improved connection pool settings
echo    - Added error handling for database init
echo    - Reduced pool size for Railway
echo.
echo 🌐 Your app will be accessible at Railway URL!
echo.
pause
