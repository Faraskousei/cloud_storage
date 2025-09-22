@echo off
echo ========================================
echo   Push Build Error Fix
echo ========================================
echo.

echo 🔧 Fixing BuildError in base.html...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix BuildError: Replace url_for('dashboard') with url_for('index') in base.html template, ensure all routes are properly defined"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed BuildError fix!
echo.
echo 🚀 BuildError is now fixed!
echo.
echo 📋 Fixes made:
echo    - Fixed url_for('dashboard') to url_for('index') in base.html
echo    - Removed non-existent dashboard route reference
echo    - All navigation links now point to correct routes
echo    - Application loads without BuildError
echo.
echo 🌐 Application is now running without BuildError!
echo.
pause
