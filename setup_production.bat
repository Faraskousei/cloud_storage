@echo off
echo ========================================
echo   Production Setup - Cloud Storage
echo ========================================
echo.

echo 🔧 Setting up for production deployment...
echo.

echo 📁 Creating production files...
if not exist "requirements_production.txt" (
    echo ❌ requirements_production.txt not found!
    echo 📥 Please create production requirements file
    pause
    exit /b 1
)

echo ✅ Production files ready
echo.

echo 🗄️  Setting up production database...
if exist "venv\Scripts\python.exe" (
    echo ✅ Python virtual environment found
    echo.
    echo 🔧 Running production database setup...
    venv\Scripts\python.exe setup_production_db.py
) else (
    echo ❌ Virtual environment not found!
    echo.
    echo 📥 Create virtual environment first:
    echo    py -m venv venv
    echo    venv\Scripts\activate
    echo    pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo.
echo 🚀 Production setup completed!
echo.
echo 📋 Next steps:
echo    1. Choose hosting platform (Railway, Render, PythonAnywhere)
echo    2. Create GitHub repository
echo    3. Upload your code
echo    4. Configure environment variables
echo    5. Deploy your application
echo.
echo 📖 Read deployment guides:
echo    - railway_deploy.md
echo    - render_deploy.md
echo    - pythonanywhere_deploy.md
echo.
echo 🌐 Your app will be accessible worldwide!
echo.
pause
