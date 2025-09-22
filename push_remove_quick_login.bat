@echo off
echo ========================================
echo   Remove Quick Login Feature
echo ========================================
echo.

echo 🔧 Removing quick login admin and frxadz...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Remove quick login feature: Removed admin and frxadz quick login buttons, CSS styles, and JavaScript functions from login page"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully removed quick login feature!
echo.
echo 🚀 Login page is now cleaner!
echo.
echo 📋 Changes made:
echo    - Removed demo section with quick login buttons
echo    - Removed quickLogin JavaScript function
echo    - Removed CSS styles for quick login buttons
echo    - Updated button selectors in JavaScript
echo.
echo 🔐 Login page is now simplified!
echo.
pause
