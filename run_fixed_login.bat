@echo off
echo ========================================
echo   Cloud Storage - Fixed Login System
echo ========================================
echo.

echo 🔧 Menggunakan Python dari virtual environment...
if exist "venv\Scripts\python.exe" (
    echo ✅ Python virtual environment ditemukan
    echo.
    echo 🚀 Menjalankan aplikasi dengan sistem login yang sudah diperbaiki...
    echo 📁 Upload folder: %cd%\uploads
    echo 🌐 Akses aplikasi di: http://localhost:5000
    echo 🔑 Halaman login akan muncul pertama kali
    echo 👤 Demo login: admin/password atau user/password
    echo ⏹️  Tekan Ctrl+C untuk menghentikan server
    echo ========================================
    echo.
    
    REM Set environment variable untuk development
    set FLASK_ENV=development
    venv\Scripts\python.exe run.py
) else (
    echo ❌ Virtual environment tidak ditemukan!
    echo.
    echo 📥 Buat virtual environment terlebih dahulu:
    echo    py -m venv venv
    echo    venv\Scripts\activate
    echo    pip install -r requirements.txt
    echo.
    pause
)

echo.
echo 📝 Server dihentikan.
pause
