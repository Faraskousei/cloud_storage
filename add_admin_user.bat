@echo off
echo ========================================
echo   Menambahkan User Admin Baru
echo ========================================
echo.

echo 🔧 Menggunakan Python dari virtual environment...
if exist "venv\Scripts\python.exe" (
    echo ✅ Python virtual environment ditemukan
    echo.
    echo 👤 Menambahkan user admin: frxadz
    echo 🔑 Password: admin
    echo 👥 Team: Team Development
    echo 🔐 Role: Administrator
    echo.
    echo ========================================
    echo.
    
    venv\Scripts\python.exe add_admin_user.py
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
echo 📝 Proses selesai.
pause
