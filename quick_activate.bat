@echo off
echo Mengaktifkan virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment aktif!
echo.
echo 📝 Command yang tersedia:
echo    pip install -r requirements.txt
echo    python run.py
echo.
cmd /k
