@echo off
echo ========================================
echo   Push Flask before_first_request Fix
echo ========================================
echo.

echo 🔧 Fixing Flask before_first_request error...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix Flask before_first_request: Remove deprecated decorator and use direct initialization"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed Flask fix!
echo.
echo 🚀 Railway deployment should work now!
echo.
echo 📋 Changes made:
echo    - Removed @app.before_first_request decorator
echo    - Used direct database initialization
echo    - Added proper error handling
echo    - Compatible with Flask 2.3.3
echo.
echo 🌐 Your app will be accessible at Railway URL!
echo.
pause
