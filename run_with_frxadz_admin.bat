@echo off
echo ========================================
echo   Cloud Storage - Frxadz Admin
echo ========================================
echo.

echo 🔧 Menggunakan Python dari virtual environment...
if exist "venv\Scripts\python.exe" (
    echo ✅ Python virtual environment ditemukan
    echo.
    echo 🚀 Menjalankan aplikasi dengan user admin baru...
    echo 📁 Upload folder: %cd%\uploads
    echo 🌐 Akses aplikasi di: http://localhost:5000
    echo 🔑 Login: http://localhost:5000/login
    echo 📝 Register: http://localhost:5000/register
    echo.
    echo 👤 Admin Users:
    echo    - Username: admin, Password: admin123
    echo    - Username: frxadz, Password: admin
    echo.
    echo 📄 PDF Viewer: Klik "View" pada file PDF
    echo 🦶 Footer: Tetap di posisi bawah
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
