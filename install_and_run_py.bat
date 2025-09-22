@echo off
setlocal enabledelayedexpansion
echo ========================================
echo   Cloud Storage Sederhana - Installer
echo ========================================
echo.

echo [1/5] Memeriksa Python...
py --version >nul 2>&1
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
py --version

echo.
echo [2/5] Memeriksa pip...
py -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip tidak ditemukan!
    echo 📥 Menginstall pip...
    py -m ensurepip --upgrade
    if %errorlevel% neq 0 (
        echo ❌ Gagal menginstall pip!
        pause
        exit /b 1
    )
)

echo ✅ pip tersedia!

echo.
echo [3/5] Membuat virtual environment...
if not exist "venv" (
    echo 📦 Membuat virtual environment...
    py -m venv venv
    if %errorlevel% neq 0 (
        echo ❌ Gagal membuat virtual environment!
        pause
        exit /b 1
    )
    echo ✅ Virtual environment dibuat
) else (
    echo ✅ Virtual environment sudah ada
)

echo.
echo [4/5] Mengaktifkan virtual environment dan install dependencies...
echo 📦 Mengaktifkan virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ Gagal mengaktifkan virtual environment!
    pause
    exit /b 1
)

echo 📦 Upgrade pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo ⚠️  Warning: Gagal upgrade pip, melanjutkan dengan pip yang ada...
)

echo 📦 Install dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Gagal install dependencies!
    echo.
    echo 🔧 Mencoba install satu per satu...
    pip install Flask==2.3.3
    pip install Werkzeug==2.3.7
    pip install Jinja2==3.1.2
    pip install MarkupSafe==2.1.3
    pip install itsdangerous==2.1.2
    pip install click==8.1.7
    pip install blinker==1.6.3
    pip install Flask-SQLAlchemy==3.0.5
    pip install Flask-Login==0.6.3
    pip install Flask-Migrate==4.0.5
    pip install PyMySQL==1.1.0
    pip install cryptography==41.0.7
    pip install bcrypt==4.0.1
)

echo.
echo [5/5] Menjalankan aplikasi...
echo.
echo 🚀 Cloud Storage Server dimulai...
echo 📁 Upload folder: %cd%\uploads
echo 🌐 Akses aplikasi di: http://localhost:5000
echo ⏹️  Tekan Ctrl+C untuk menghentikan server
echo ========================================
echo.

python run.py

echo.
echo 📝 Server dihentikan.
pause
