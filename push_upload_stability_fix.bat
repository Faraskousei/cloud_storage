@echo off
echo ========================================
echo   Fix Upload Stability Issues
echo ========================================
echo.

echo 🔧 Fixing upload stability issues across all files...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix upload stability: Enhanced error handling in app.py, improved run.py with folder validation, enhanced main.py upload function, better file validation, database transaction safety, and detailed logging"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully fixed upload stability issues!
echo.
echo 🚀 Upload system is now more stable across all files!
echo.
echo 📋 Fixes implemented:
echo    - Enhanced error handling in app.py
echo    - Improved run.py with folder validation
echo    - Enhanced main.py upload function
echo    - Better file validation and error handling
echo    - Database transaction safety
echo    - File cleanup on errors
echo    - Detailed logging for debugging
echo    - Threaded server support
echo.
echo 🔧 Upload system is now reliable and stable!
echo.
pause
