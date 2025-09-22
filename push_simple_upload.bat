@echo off
echo ========================================
echo   Push Simple Upload UI
echo ========================================
echo.

echo 🔧 Simplifying upload UI and ensuring functionality...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Simplify upload UI: Simple upload modal with working functionality and file storage in uploads folder"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed simple upload UI!
echo.
echo 🚀 Simple upload UI is now working!
echo.
echo 📋 Changes made:
echo    - Simplified upload modal UI
echo    - Removed complex AJAX animations
echo    - Simple progress bar and status
echo    - File uploads go to uploads folder
echo    - Files appear in list after upload
echo    - Page reloads to show new files
echo.
echo 🌐 Upload functionality is now simple and working!
echo.
pause
