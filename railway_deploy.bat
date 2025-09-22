@echo off
echo ========================================
echo   Railway Deployment Setup
echo ========================================
echo.

echo 🔧 Setting up Railway deployment...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Railway deployment: Add PostgreSQL database configuration and environment setup"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed to GitHub!
echo.
echo 🚀 Next steps for Railway deployment:
echo.
echo 1. Go to https://railway.app
echo 2. Sign up with GitHub
echo 3. Create new project
echo 4. Connect your GitHub repository
echo 5. Add PostgreSQL database
echo 6. Set environment variables
echo 7. Deploy and test!
echo.
echo 📋 Check RAILWAY_DEPLOYMENT_GUIDE.md for detailed instructions
echo.
echo 🌐 Your app will be live on Railway with PostgreSQL database!
echo.
pause
