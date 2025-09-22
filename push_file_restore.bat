@echo off
echo ========================================
echo   Push File Restore Fix
echo ========================================
echo.

echo 🔧 Restoring files from uploads folder to database...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix file display: Restore files from uploads folder to database with download keys"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed file restore fix!
echo.
echo 🚀 Files from uploads folder are now visible!
echo.
echo 📋 Changes made:
echo    - Restored files from uploads folder to database
echo    - Added download keys for all files
echo    - Files now appear in the application
echo    - Copy link feature available for all files
echo.
echo 🌐 Your uploaded files should now be visible!
echo.
pause
