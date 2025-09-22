@echo off
echo ========================================
echo   Setup Remote Repository - Cloud Storage
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

echo 📋 Setup Remote Repository
echo.
echo 1. Go to https://github.com
echo 2. Sign in to your account
echo 3. Click "New repository"
echo 4. Repository name: cloud-storage
echo 5. Description: Cloud Storage Application
echo 6. Make it Public or Private
echo 7. Don't initialize with README
echo 8. Click "Create repository"
echo.
echo 🔗 After creating repository, enter your repository URL:
echo    Format: https://github.com/username/cloud-storage.git
echo.

set /p repo_url="Enter your repository URL: "

if "%repo_url%"=="" (
    echo ❌ Repository URL tidak boleh kosong!
    echo.
    pause
    exit /b 1
)

echo.
echo 🔧 Setting up remote repository...
git remote add origin %repo_url%

echo ✅ Remote repository added!
echo.

echo 🔍 Verifying remote repository...
git remote -v

echo.
echo 🚀 Pushing to GitHub...
git push -u origin main

echo.
echo ✅ Successfully pushed to GitHub!
echo.
echo 🌐 Your repository is now accessible at:
echo    %repo_url%
echo.
echo 🚀 Next steps:
echo    1. Check your repository on GitHub
echo    2. Verify all files are uploaded
echo    3. Test deployment to hosting platform
echo    4. Share your repository with others
echo.
pause
