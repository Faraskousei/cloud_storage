@echo off
echo ========================================
echo   Admin Register System
echo ========================================
echo.

echo 🔧 Implementing admin-only register system...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Implement admin-only register system: Removed public register, added admin register page, updated navbar with admin controls, restricted user creation to admin only"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully implemented admin-only register system!
echo.
echo 🚀 Register system is now admin-only!
echo.
echo 📋 Changes made:
echo    - Removed public register route and page
echo    - Removed register link from login page
echo    - Added admin register page with user management
echo    - Added admin register route with validation
echo    - Updated navbar with admin controls
echo    - Restricted user creation to admin only
echo.
echo 🔐 User registration is now controlled by admin!
echo.
pause
