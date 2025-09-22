@echo off
echo ========================================
echo   Push Download Link Feature
echo ========================================
echo.

echo 🔧 Adding copy link feature for direct download...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Add copy link feature: Secure download links with unique keys for all files"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed download link feature!
echo.
echo 🚀 Copy link feature is now available!
echo.
echo 📋 Features added:
echo    - Added download_key field to File model
echo    - Secure download route with key validation
echo    - Copy link button for each file
echo    - Notification system for copy feedback
echo    - Database reset with new schema
echo.
echo 🌐 Users can now copy download links for any file!
echo.
pause
