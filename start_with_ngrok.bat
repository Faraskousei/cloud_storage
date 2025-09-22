@echo off
echo ========================================
echo   Start Cloud Storage with NGROK
echo ========================================
echo.

echo 🔧 Starting Flask application...
start "Flask App" cmd /k "venv\Scripts\python.exe run.py"

echo ⏳ Waiting for Flask to start...
timeout /t 5

echo 🌐 Starting NGROK...
start "NGROK" cmd /k "ngrok http 5000"

echo.
echo ✅ Application started with NGROK!
echo 🌐 Check NGROK output for public URL
echo 📱 You can now access your app from anywhere!
echo.
echo 🔧 NGROK Web Interface: http://127.0.0.1:4040
echo 🌐 Local URL: http://localhost:5000
echo.
echo ⏹️  Press any key to continue...
pause
