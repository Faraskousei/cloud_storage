@echo off
echo ========================================
echo   Cloud Storage - MySQL Integration
echo ========================================
echo.

echo 🔧 Menggunakan Python dari virtual environment...
if exist "venv\Scripts\python.exe" (
    echo ✅ Python virtual environment ditemukan
    echo.
    echo 📊 Inisialisasi database MySQL...
    echo.
    
    REM Set environment variable untuk development
    set FLASK_ENV=development
    
    echo 🔄 Menjalankan inisialisasi database...
    venv\Scripts\python.exe init_database.py
    
    if %errorlevel% neq 0 (
        echo ❌ Gagal inisialisasi database!
        echo.
        echo 🔧 Pastikan:
        echo    1. MySQL server sudah running
        echo    2. Database 'cloud_storage' sudah dibuat
        echo    3. Jalankan setup_database.sql terlebih dahulu
        echo.
        pause
        exit /b 1
    )
    
    echo.
    echo 🚀 Menjalankan aplikasi dengan MySQL...
    echo 📁 Upload folder: %cd%\uploads
    echo 🌐 Akses aplikasi di: http://localhost:5000
    echo 🔑 Login: admin/admin123
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
