@echo off
echo ========================================
echo   Push Railway Fix to GitHub
echo ========================================
echo.

echo 🔧 Pushing Railway deployment fixes...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Fix Railway deployment: Add gunicorn, wsgi.py, and PostgreSQL config"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed Railway fixes!
echo.
echo 🚀 Railway deployment should work now!
echo.
echo 📋 Next steps in Railway:
echo    1. Go to Railway Dashboard
echo    2. Select your project
echo    3. Go to Variables tab
echo    4. Add environment variables:
echo       - FLASK_ENV=production
echo       - SECRET_KEY=211093fcccd2d8da90923395106d1e4ff85a9b13fd605c6edaabba20afec56ae
echo    5. Add PostgreSQL database
echo    6. Redeploy your application
echo.
echo 🌐 Your app will be accessible at Railway URL!
echo.
pause
