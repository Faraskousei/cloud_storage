@echo off
echo ========================================
echo   Setup dan Aktifkan Virtual Environment
echo ========================================
echo.

echo [1/3] Memeriksa Python...
py --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python tidak ditemukan!
    echo 📥 Install Python dari: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✅ Python tersedia!

echo.
echo [2/3] Membuat virtual environment...
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
echo [3/3] Mengaktifkan virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ Gagal mengaktifkan virtual environment!
    pause
    exit /b 1
)

echo ✅ Virtual environment berhasil diaktifkan!
echo.
echo 📝 Sekarang Anda bisa menjalankan:
echo    - pip install -r requirements.txt
echo    - python run.py
echo.
echo 💡 Untuk keluar dari virtual environment, ketik: deactivate
echo.
echo 🚀 Menjalankan command prompt dengan virtual environment aktif...
cmd /k
