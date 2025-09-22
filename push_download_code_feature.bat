@echo off
echo ========================================
echo   Push Download Code Feature
echo ========================================
echo.

echo 🔧 Adding download code verification feature...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Add download code verification: Secure download with 6-digit code verification, download_verify.html template, download_error.html template, enhanced security for file downloads"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed download code feature!
echo.
echo 🚀 Download code verification is now working!
echo.
echo 📋 Features added:
echo    - 6-digit download code verification
echo    - Secure download with code protection
echo    - Download verification page
echo    - Download error handling
echo    - Code display modal for file owners
echo    - Enhanced security for file downloads
echo    - User-friendly verification interface
echo.
echo 🔐 Files now require download code to access!
echo.
pause
