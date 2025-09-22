@echo off
echo ========================================
echo   Push Remove Key Icons
echo ========================================
echo.

echo 🔧 Pushing remove key icons changes...
echo.

echo 📦 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Remove key icons from UI: Removed key button from file cards, removed key icons from modal headers, removed CSS for key button, removed old showDownloadCode function, kept rotating keys functionality"

echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Successfully removed key icons!
echo.
echo 🚀 Key icons removed from UI!
echo 💡 Rotating keys functionality preserved!
echo.
echo 📋 Changes made:
echo    - Removed key button from file cards
echo    - Removed key icons from modal headers
echo    - Removed CSS for key button
echo    - Removed old showDownloadCode function
echo    - Kept rotating keys functionality
echo    - Kept showDownloadCodeModal function
echo.
echo 🔧 UI is now cleaner without key icons!
echo.
pause
