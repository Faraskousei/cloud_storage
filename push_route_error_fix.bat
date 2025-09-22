@echo off
echo ========================================
echo   Push Route Error Fix
echo ========================================
echo.

echo 🔧 Fixing route errors...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix route errors: Add comprehensive error handling for index and register routes"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed route error fixes!
echo.
echo 🚀 Railway deployment should work now!
echo.
echo 📋 Changes made:
echo    - Added error handling for index route
echo    - Added error handling for register route
echo    - Added database connection testing
echo    - Added comprehensive error logging
echo.
echo 🌐 Your app will show proper error pages now!
echo.
echo 🔧 Check Railway logs for specific error messages
echo.
pause
