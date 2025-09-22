@echo off
echo ========================================
echo   Remove Purple Frame Fix
echo ========================================
echo.

echo 🔧 Removing purple frame from background...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Remove purple frame: Simplify background to clean white/gray"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully removed purple frame!
echo.
echo 🚀 Background is now clean and simple!
echo.
echo 📋 Changes made:
echo    - Removed complex gradient background
echo    - Simplified to clean white/gray background
echo    - Removed gradientShift animation
echo    - Cleaned up navbar styling
echo.
echo 🌐 Your app now has a clean, professional look!
echo.
pause
