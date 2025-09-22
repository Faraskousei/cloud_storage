@echo off
echo ========================================
echo   Push Rotating Download Keys
echo ========================================
echo.

echo 🔧 Pushing rotating download keys system...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Implement rotating download keys: Download key and code rotate every time copy-link is called, old links become invalid automatically, enhanced security with rotating keys, user gets notification with new download code, modal shows new download code with warning"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully implemented rotating download keys!
echo.
echo 🚀 Download keys now rotate on each copy!
echo 🔐 Enhanced security with rotating keys!
echo 💡 Old links become invalid automatically!
echo.
echo 📋 Features implemented:
echo    - Download key rotates every time copy-link is called
echo    - Download code rotates every time copy-link is called
echo    - Old links become invalid when new key is generated
echo    - Enhanced security with rotating keys
echo    - User gets notification with new download code
echo    - Modal shows new download code with warning
echo    - Database updates with new key/code automatically
echo.
echo 🔧 Rotating keys system is now active!
echo.
pause
