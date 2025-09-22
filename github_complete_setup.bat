@echo off
echo ========================================
echo   GitHub Complete Setup - Cloud Storage
echo ========================================
echo.

echo 🔧 Checking Git installation...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git tidak terinstall!
    echo.
    echo 📥 Langkah-langkah install Git:
    echo    1. Download dari: https://git-scm.com/download/win
    echo    2. Install dengan default settings
    echo    3. Restart command prompt/PowerShell
    echo    4. Jalankan script ini lagi
    echo.
    echo 🌐 Atau gunakan cara manual:
    echo    1. Go to https://github.com
    echo    2. Create new repository
    echo    3. Upload files via web interface
    echo.
    pause
    exit /b 1
)

echo ✅ Git sudah terinstall!
echo.

echo 📁 Initializing Git repository...
git init

echo 📦 Adding files to Git...
git add .

echo 💾 Creating initial commit...
git commit -m "Initial commit: Cloud Storage Application"

echo.
echo 🚀 Repository ready for GitHub!
echo.
echo 📋 Next steps:
echo    1. Go to https://github.com
echo    2. Sign in to your account
echo    3. Click "New repository"
echo    4. Repository name: cloud-storage
echo    5. Description: Cloud Storage Application
echo    6. Make it Public or Private
echo    7. Don't initialize with README
echo    8. Click "Create repository"
echo.
echo 🔗 After creating repository, run:
echo    git remote add origin https://github.com/username/cloud-storage.git
echo    git push -u origin main
echo.
echo 🌐 Your repository will be accessible worldwide!
echo.
echo 📖 Read github_manual_setup.md for detailed guide
echo.
pause
