@echo off
echo ========================================
echo   Mengaktifkan Virtual Environment
echo ========================================
echo.

echo 🔧 Mengaktifkan virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment berhasil diaktifkan!
    echo.
    echo 📝 Sekarang Anda bisa menjalankan:
    echo    - pip install -r requirements.txt
    echo    - python run.py
    echo.
    echo 💡 Untuk keluar dari virtual environment, ketik: deactivate
    echo.
    cmd /k
) else (
    echo ❌ Virtual environment tidak ditemukan!
    echo.
    echo 📥 Buat virtual environment terlebih dahulu:
    echo    py -m venv venv
    echo.
    pause
)
