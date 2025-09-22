@echo off
echo ========================================
echo   Cloud Storage Sederhana - Installer
echo ========================================
echo.

echo [1/4] Memeriksa Python...
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
echo [2/4] Membuat virtual environment...
if not exist "venv" (
    python -m venv venv
    echo ✅ Virtual environment dibuat
) else (
    echo ✅ Virtual environment sudah ada
)

echo.
echo [3/4] Mengaktifkan virtual environment dan install dependencies...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo [4/4] Menjalankan aplikasi...
echo.
echo 🚀 Cloud Storage Server dimulai...
echo 📁 Upload folder: %cd%\uploads
echo 🌐 Akses aplikasi di: http://localhost:5000
echo ⏹️  Tekan Ctrl+C untuk menghentikan server
echo ========================================
echo.

python run.py

pause
