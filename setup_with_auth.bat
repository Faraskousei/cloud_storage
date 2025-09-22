@echo off
echo ========================================
echo   Cloud Storage with Authentication
echo   Setup Script for Windows
echo ========================================
echo.

echo [1/6] Memeriksa Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python tidak ditemukan!
    echo.
    echo 📥 Silakan install Python terlebih dahulu:
    echo    https://www.python.org/downloads/
    echo.
    echo ✅ Pastikan centang "Add Python to PATH" saat instalasi
    echo.
    pause
    exit /b 1
)

echo ✅ Python ditemukan!
python --version

echo.
echo [2/6] Memeriksa XAMPP MySQL...
echo.
echo ⚠️  PENTING: Pastikan XAMPP sudah diinstall dan MySQL service running!
echo.
echo 📋 Langkah-langkah:
echo    1. Buka XAMPP Control Panel
echo    2. Start MySQL service
echo    3. Buka phpMyAdmin (http://localhost/phpmyadmin)
echo    4. Import file setup_database.sql
echo.
echo 🔧 Atau jalankan perintah berikut di MySQL:
echo    mysql -u root -p < setup_database.sql
echo.
pause

echo.
echo [3/6] Membuat virtual environment...
if not exist "venv" (
    python -m venv venv
    echo ✅ Virtual environment dibuat
) else (
    echo ✅ Virtual environment sudah ada
)

echo.
echo [4/6] Mengaktifkan virtual environment dan install dependencies...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo [5/6] Membuat folder uploads untuk setiap team...
if not exist "uploads" mkdir uploads
if not exist "uploads\team_1" mkdir uploads\team_1
if not exist "uploads\team_2" mkdir uploads\team_2
if not exist "uploads\team_3" mkdir uploads\team_3
echo ✅ Folder uploads untuk teams dibuat

echo.
echo [6/6] Menjalankan aplikasi...
echo.
echo 🚀 Cloud Storage dengan Authentication dimulai...
echo 📁 Upload folder: %cd%\uploads
echo 🌐 Akses aplikasi di: http://localhost:5000
echo 👤 Login dengan: username='admin', password='admin123'
echo 👥 Teams: Development, Marketing, Operations
echo ========================================
echo.

python main.py

pause
