@echo off
echo ========================================
echo   Cloud Storage - Quick Start
echo ========================================
echo.

echo 🔧 Mengaktifkan virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment diaktifkan
) else (
    echo ❌ Virtual environment tidak ditemukan!
    echo 📥 Jalankan install_and_run_fixed.bat terlebih dahulu
    pause
    exit /b 1
)

echo.
echo 🚀 Menjalankan aplikasi...
echo 📁 Upload folder: %cd%\uploads
echo 🌐 Akses aplikasi di: http://localhost:5000
echo ⏹️  Tekan Ctrl+C untuk menghentikan server
echo ========================================
echo.

python run.py

pause
