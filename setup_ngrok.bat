@echo off
echo ========================================
echo   NGROK Setup for Cloud Storage
echo ========================================
echo.

echo 🔧 Setting up NGROK for Cloud Storage...
echo.

echo 📋 Steps to setup NGROK:
echo.
echo 1. Download NGROK from: https://ngrok.com/download
echo 2. Extract ngrok.exe to C:\ngrok\
echo 3. Create account at: https://ngrok.com
echo 4. Get your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken
echo 5. Run: ngrok config add-authtoken YOUR_AUTHTOKEN
echo.

echo 🔧 Alternative - Install via Chocolatey:
echo    choco install ngrok
echo.

echo 🔧 Alternative - Install via Scoop:
echo    scoop install ngrok
echo.

echo 📋 After setup, you can use:
echo    start_with_ngrok.bat    - Start app with NGROK
echo    stop_all_services.bat   - Stop all services
echo.

echo ⏹️  Press any key to continue...
pause
