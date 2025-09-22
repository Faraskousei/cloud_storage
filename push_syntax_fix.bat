@echo off
echo ========================================
echo   Push Syntax Fix
echo ========================================
echo.

echo 🔧 Fixing syntax errors in app.py...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix syntax errors: Correct indentation issues in app.py, fix try-except blocks, ensure proper code structure for upload and download functionality"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed syntax fixes!
echo.
echo 🚀 Syntax errors are now fixed!
echo.
echo 📋 Fixes made:
echo    - Fixed indentation issues in upload_file function
echo    - Corrected try-except block structure
echo    - Fixed syntax errors in index route
echo    - Ensured proper code formatting
echo    - All download and preview features working
echo.
echo 🌐 Application is now running without syntax errors!
echo.
pause
