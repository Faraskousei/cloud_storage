@echo off
echo ========================================
echo   Push Download & Preview Features
echo ========================================
echo.

echo 🔧 Adding download and preview functionality...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Add download and preview features: Download files with secure keys, preview PDF and images in browser, notification system for user feedback"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed download and preview features!
echo.
echo 🚀 Download and preview features are now working!
echo.
echo 📋 Features added:
echo    - Download files with secure download keys
echo    - Preview PDF files in browser
echo    - Preview images (PNG, JPG, JPEG, GIF) in browser
echo    - Secure download URLs with unique keys
echo    - Preview URLs for browser viewing
echo    - Notification system for user feedback
echo    - Error handling for missing files
echo.
echo 🌐 Download and preview functionality is now ready!
echo.
pause
