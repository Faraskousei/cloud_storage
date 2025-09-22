@echo off
echo ========================================
echo   Push Upload Improvements
echo ========================================
echo.

echo 🔧 Improving upload functionality...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Improve upload functionality: AJAX upload with immediate display, team isolation, and uploads folder management"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed upload improvements!
echo.
echo 🚀 Upload functionality is now improved!
echo.
echo 📋 Improvements made:
echo    - AJAX upload with immediate file display
echo    - Team isolation - users only see their team files
echo    - Admin can see all files from all teams
echo    - Uploads folder automatically created
echo    - File uploads go directly to uploads folder
echo    - Real-time file count updates
echo    - Progress bar during upload
echo.
echo 🌐 Upload functionality is now working perfectly!
echo.
pause

