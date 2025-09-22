@echo off
echo ========================================
echo   Mengaktifkan Virtual Environment
echo ========================================
echo.

echo 🔧 Mengaktifkan virtual environment...
if exist "venv\Scripts\activate.bat" (
    echo ✅ Menggunakan activate.bat...
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment berhasil diaktifkan!
) else if exist "venv\Scripts\Activate.ps1" (
    echo ⚠️  PowerShell execution policy terbatas
    echo 🔧 Menggunakan cara alternatif...
    
    echo 📝 Untuk mengaktifkan virtual environment, jalankan salah satu:
    echo.
    echo 1. Buka Command Prompt (cmd) dan jalankan:
    echo    venv\Scripts\activate.bat
    echo.
    echo 2. Atau ubah PowerShell execution policy:
    echo    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    echo    venv\Scripts\Activate.ps1
    echo.
    echo 3. Atau gunakan Python langsung:
    echo    venv\Scripts\python.exe run.py
    echo.
    pause
    exit /b 1
) else (
    echo ❌ Virtual environment tidak ditemukan!
    echo.
    echo 📥 Buat virtual environment terlebih dahulu:
    echo    py -m venv venv
    echo.
    pause
    exit /b 1
)

echo.
echo 📝 Sekarang Anda bisa menjalankan:
echo    - pip install -r requirements.txt
echo    - python run.py
echo.
echo 💡 Untuk keluar dari virtual environment, ketik: deactivate
echo.
cmd /k
