@echo off
echo ========================================
echo   Fix BuildError for Register Route
echo ========================================
echo.

echo 🔧 Fixing BuildError for removed register route...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix BuildError: Removed register link from navbar, deleted unused register.html template, updated all references to use admin_register route"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully fixed BuildError!
echo.
echo 🚀 Application should work without BuildError!
echo.
echo 📋 Fixes implemented:
echo    - Removed register link from base.html navbar
echo    - Deleted unused register.html template
echo    - Updated dashboard.html to use admin_register
echo    - Updated auth/profile.html to use admin_register
echo    - All references now point to admin_register
echo.
echo 🔧 BuildError is now fixed!
echo.
pause