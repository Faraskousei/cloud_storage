@echo off
echo ========================================
echo   Push NGROK Tutorial
echo ========================================
echo.

echo 🔧 Adding NGROK tutorial and scripts...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Add NGROK tutorial: Complete guide for running app with NGROK"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed NGROK tutorial!
echo.
echo 🚀 NGROK tutorial and scripts are now available!
echo.
echo 📋 Files added:
echo    - NGROK_TUTORIAL.md - Complete NGROK guide
echo    - start_with_ngrok.bat - Start app with NGROK
echo    - stop_all_services.bat - Stop all services
echo    - setup_ngrok.bat - NGROK setup guide
echo.
echo 🌐 Use these scripts to run your app with NGROK!
echo.
echo 🔧 Quick start:
echo    1. Run setup_ngrok.bat for setup instructions
echo    2. Run start_with_ngrok.bat to start app with NGROK
echo    3. Run stop_all_services.bat to stop everything
echo.
pause
