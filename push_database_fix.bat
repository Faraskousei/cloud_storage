@echo off
echo ========================================
echo   Push Database Fix for Railway
echo ========================================
echo.

echo 🔧 Fixing Railway database configuration...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix Railway database: Switch from MySQL to PostgreSQL with proper connection handling"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed database fixes!
echo.
echo 🚀 Railway deployment should work now!
echo.
echo 📋 Changes made:
echo    - Updated config.py for Railway PostgreSQL
echo    - Added SQLite fallback for testing
echo    - Improved database connection handling
echo    - Added Railway database setup script
echo.
echo 🌐 Railway will now use PostgreSQL instead of MySQL!
echo.
echo 🔧 Check Railway logs for database connection success
echo.
pause
