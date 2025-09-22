@echo off
echo ========================================
echo   Push Database Tools for Railway
echo ========================================
echo.

echo 🔧 Adding database tools for Railway...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Add Railway database tools: dump_db, restore_db, backup_railway"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully pushed database tools!
echo.
echo 🚀 Railway database tools are now available!
echo.
echo 📋 Tools added:
echo    - dump_db.py - Dump Railway PostgreSQL database
echo    - restore_db.py - Restore Railway PostgreSQL database
echo    - backup_railway.py - Backup Railway PostgreSQL database
echo.
echo 🌐 Use these tools to manage your Railway database!
echo.
echo 🔧 Commands:
echo    python dump_db.py full    - Full database dump
echo    python dump_db.py data    - Data-only dump
echo    python restore_db.py      - Restore database
echo    python backup_railway.py  - Backup database
echo.
pause
