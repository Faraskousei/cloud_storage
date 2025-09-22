@echo off
echo ========================================
echo   Cloud Storage Sederhana - Runner
echo ========================================
echo.

echo [1/2] Mengaktifkan virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment diaktifkan
) else (
    echo ❌ Virtual environment tidak ditemukan!
    echo.
    echo 💡 Jalankan install_and_run.bat terlebih dahulu
    echo.
    pause
    exit /b 1
)

echo.
echo [2/2] Menjalankan aplikasi...
echo.
echo 🚀 Cloud Storage Server dimulai...
echo 📁 Upload folder: %cd%\uploads
echo 🌐 Akses aplikasi di: http://localhost:5000
echo ⏹️  Tekan Ctrl+C untuk menghentikan server
echo ========================================
echo.

python run.py

pause
