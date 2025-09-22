@echo off
echo ========================================
echo   Cloud Storage - Quick Start
echo ========================================
echo.

echo 🔧 Setup dan jalankan aplikasi...
echo.

REM Set environment untuk development
set FLASK_ENV=development

echo 📦 Mengaktifkan virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment aktif
) else (
    echo ❌ Virtual environment tidak ditemukan!
    echo 📥 Buat virtual environment terlebih dahulu:
    echo    py -m venv venv
    echo    venv\Scripts\activate
    echo    pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo 🚀 Menjalankan aplikasi...
echo 🌐 Akses di: http://localhost:5000
echo 🔑 Login di: http://localhost:5000/login
echo ⏹️  Tekan Ctrl+C untuk menghentikan
echo ========================================
echo.

python run.py

echo.
echo 📝 Server dihentikan.
pause