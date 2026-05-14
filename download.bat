@echo off
title XCRYP-IP INSTALLER
color 0B

echo ====================================
echo        XCRYP-IP INSTALLER
echo ====================================
echo.

python --version >nul 2>&1

if %errorlevel% neq 0 (
    echo [!] Python is not installed!
    pause
    exit
)

echo [+] Installing required libraries...
echo.

pip install requests
pip install colorama

echo.
echo [+] Installation completed!
pause