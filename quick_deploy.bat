@echo off
echo ========================================
echo   Quick Deploy - Cloud Storage
echo ========================================
echo.

echo 🚀 Quick deployment options:
echo.
echo 1. Railway (Recommended)
echo    - Free: 500 hours/month
echo    - Database: PostgreSQL included
echo    - Domain: Custom domain support
echo    - SSL: Automatic HTTPS
echo.
echo 2. Render
echo    - Free: 750 hours/month
echo    - Database: PostgreSQL included
echo    - Domain: Custom domain support
echo    - SSL: Automatic HTTPS
echo.
echo 3. PythonAnywhere
echo    - Free: 1 web app
echo    - Database: MySQL included
echo    - Domain: pythonanywhere.com
echo    - SSL: Available
echo.
echo 4. Heroku (Limited)
echo    - Free: 550-1000 hours/month
echo    - Database: PostgreSQL addon
echo    - Domain: herokuapp.com
echo    - SSL: Automatic HTTPS
echo.

set /p choice="Choose deployment option (1-4): "

if "%choice%"=="1" (
    echo.
    echo 🚀 Deploying to Railway...
    echo.
    echo 📋 Steps:
    echo    1. Go to https://railway.app
    echo    2. Sign up with GitHub
    echo    3. Create new project
    echo    4. Connect your GitHub repository
    echo    5. Add PostgreSQL database
    echo    6. Set environment variables
    echo    7. Deploy!
    echo.
    echo 📖 Read railway_deploy.md for detailed guide
    echo.
    start https://railway.app
) else if "%choice%"=="2" (
    echo.
    echo 🚀 Deploying to Render...
    echo.
    echo 📋 Steps:
    echo    1. Go to https://render.com
    echo    2. Sign up with GitHub
    echo    3. Create new web service
    echo    4. Connect your GitHub repository
    echo    5. Add PostgreSQL database
    echo    6. Set environment variables
    echo    7. Deploy!
    echo.
    echo 📖 Read render_deploy.md for detailed guide
    echo.
    start https://render.com
) else if "%choice%"=="3" (
    echo.
    echo 🚀 Deploying to PythonAnywhere...
    echo.
    echo 📋 Steps:
    echo    1. Go to https://pythonanywhere.com
    echo    2. Sign up for free account
    echo    3. Upload your files
    echo    4. Install dependencies
    echo    5. Create MySQL database
    echo    6. Create web app
    echo    7. Configure static files
    echo    8. Deploy!
    echo.
    echo 📖 Read pythonanywhere_deploy.md for detailed guide
    echo.
    start https://pythonanywhere.com
) else if "%choice%"=="4" (
    echo.
    echo 🚀 Deploying to Heroku...
    echo.
    echo 📋 Steps:
    echo    1. Go to https://heroku.com
    echo    2. Sign up for free account
    echo    3. Install Heroku CLI
    echo    4. Create Heroku app
    echo    5. Add PostgreSQL addon
    echo    6. Set environment variables
    echo    7. Deploy!
    echo.
    echo 📖 Read DEPLOYMENT_GUIDE.md for detailed guide
    echo.
    start https://heroku.com
) else (
    echo.
    echo ❌ Invalid choice!
    echo.
    echo Please choose 1, 2, 3, or 4
    echo.
    pause
    goto :eof
)

echo.
echo 🎉 Deployment guide opened!
echo.
echo 📝 Remember to:
echo    - Set SECRET_KEY environment variable
echo    - Configure database connection
echo    - Test your deployed app
echo    - Monitor your app performance
echo.
echo 🌐 Your app will be accessible worldwide!
echo.
pause
