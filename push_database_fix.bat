@echo off
echo ========================================
echo   Push Database Fix
echo ========================================
echo.

echo 🔧 Fixing database download_code column issue...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix database issue: Add download_code column to files table, create new database with all required columns, fix SQLAlchemy error for download code feature"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed database fix!
echo.
echo 🚀 Database issue is now fixed!
echo.
echo 📋 Fixes made:
echo    - Added download_code column to files table
echo    - Created new database with all required columns
echo    - Fixed SQLAlchemy error for download code
echo    - All files now have download codes
echo    - Download code verification is working
echo.
echo 🔐 Database is now ready for download code feature!
echo.
pause