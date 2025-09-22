@echo off
echo ========================================
echo   GitHub Setup - Cloud Storage
echo ========================================
echo.

echo 🔧 Setting up Git repository...
echo.

echo 📁 Initializing Git repository...
git init

echo 📝 Creating .gitignore...
echo ✅ .gitignore already exists

echo 📦 Adding files to Git...
git add .

echo 💾 Creating initial commit...
git commit -m "Initial commit: Cloud Storage Application"

echo.
echo 🚀 Repository ready for GitHub!
echo.
echo 📋 Next steps:
echo    1. Go to https://github.com
echo    2. Create new repository named 'cloud-storage'
echo    3. Copy repository URL
echo    4. Run: git remote add origin YOUR_REPO_URL
echo    5. Run: git push -u origin main
echo.
echo 🌐 Your repository will be accessible worldwide!
echo.
echo 📖 Read github_setup.md for detailed guide
echo.
pause
