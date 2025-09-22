@echo off
echo ========================================
echo   Push Error Handling Fix
echo ========================================
echo.

echo 🔧 Fixing Internal Server Error...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix Internal Server Error: Add error handlers, debug WSGI, and error templates"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed error handling fixes!
echo.
echo 🚀 Railway deployment should work now!
echo.
echo 📋 Changes made:
echo    - Added error handlers (500, 404, 403)
echo    - Created error.html template
echo    - Added wsgi_debug.py for debugging
echo    - Updated Procfile to use debug WSGI
echo    - Added comprehensive error handling
echo.
echo 🌐 Your app will show proper error pages now!
echo.
echo 🔧 Check Railway logs for debug information
echo.
pause
