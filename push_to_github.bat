@echo off
echo ========================================
echo   Push to GitHub - Cloud Storage
echo ========================================
echo.

echo 🔧 Pushing to GitHub...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Update Cloud Storage Application"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed to GitHub!
echo.
echo 🌐 Your repository is now updated!
echo.
echo 📖 Check your repository at:
echo    https://github.com/username/cloud-storage
echo.
pause
