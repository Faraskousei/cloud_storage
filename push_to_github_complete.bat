@echo off
echo ========================================
echo   Push to GitHub - Cloud Storage
echo ========================================
echo.

echo 🔧 Checking Git installation...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git tidak terinstall!
    echo.
    echo 📥 Install Git terlebih dahulu:
    echo    1. Download dari: https://git-scm.com/download/win
    echo    2. Install dengan default settings
    echo    3. Restart command prompt/PowerShell
    echo.
    pause
    exit /b 1
)

echo ✅ Git sudah terinstall!
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Update Cloud Storage Application"

echo.
echo 🔗 Checking remote repository...
git remote -v >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Remote repository belum di-set!
    echo.
    echo 📋 Setup remote repository:
    echo    1. Go to https://github.com
    echo    2. Create repository named 'cloud-storage'
    echo    3. Copy repository URL
    echo    4. Run: git remote add origin YOUR_REPO_URL
    echo.
    echo 🌐 Repository URL format:
    echo    https://github.com/username/cloud-storage.git
    echo.
    pause
    exit /b 1
)

echo ✅ Remote repository sudah di-set!
echo.

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
echo 🚀 Next steps:
echo    1. Check your repository on GitHub
echo    2. Verify all files are uploaded
echo    3. Test deployment to hosting platform
echo    4. Share your repository with others
echo.
pause
