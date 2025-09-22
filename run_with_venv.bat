@echo off
echo ========================================
echo   Menjalankan Aplikasi dengan Virtual Environment
echo ========================================
echo.

echo 🔧 Menggunakan Python dari virtual environment...
if exist "venv\Scripts\python.exe" (
    echo ✅ Python virtual environment ditemukan
    echo.
    echo 🚀 Menjalankan aplikasi...
    echo 📁 Upload folder: %cd%\uploads
    echo 🌐 Akses aplikasi di: http://localhost:5000
    echo ⏹️  Tekan Ctrl+C untuk menghentikan server
    echo ========================================
    echo.
    
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
