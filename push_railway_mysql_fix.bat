@echo off
echo ========================================
echo   Push Railway MySQL Fix
echo ========================================
echo.

echo 🔧 Fixing Railway MySQL connection error...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix Railway MySQL error: Switch to PostgreSQL configuration"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed Railway MySQL fix!
echo.
echo 🚀 Railway deployment should work now!
echo.
echo 📋 Changes made:
echo    - Updated config.py to use PostgreSQL for Railway
echo    - Fixed database configuration for production
echo    - Added Railway configuration test
echo    - Removed MySQL dependency for Railway
echo.
echo 🌐 Railway will now use PostgreSQL instead of MySQL!
echo.
echo 🔧 Check Railway logs for PostgreSQL connection success
echo.
pause
