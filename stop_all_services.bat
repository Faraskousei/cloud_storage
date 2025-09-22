@echo off
echo ========================================
echo   Stop Cloud Storage and NGROK
echo ========================================
echo.

echo 🛑 Stopping all services...
taskkill /f /im python.exe 2>nul
taskkill /f /im ngrok.exe 2>nul

echo ✅ All services stopped!
echo.
echo 🔧 Services stopped:
echo    - Flask application
echo    - NGROK tunnel
echo.
echo ⏹️  Press any key to continue...
pause
