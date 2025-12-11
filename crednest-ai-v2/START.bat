@echo off
echo ========================================
echo   CredNest AI v2.0 - Startup Script
echo ========================================
echo.

REM Check if MongoDB is running
echo [1/3] Checking MongoDB...
sc query MongoDB | find "RUNNING" >nul
if %errorlevel% == 0 (
    echo MongoDB is already running
) else (
    echo Starting MongoDB...
    net start MongoDB
    if %errorlevel% == 0 (
        echo MongoDB started successfully
    ) else (
        echo Failed to start MongoDB. Please start it manually.
        pause
        exit /b 1
    )
)

echo.
echo [2/3] Starting Backend Server...
cd /d "%~dp0server"
start "CredNest AI - Backend" cmd /k "npm run dev"

echo.
echo [3/3] Opening Frontend...
timeout /t 3 /nobreak >nul
start "" "%~dp0frontend-pages\index.html"

echo.
echo ========================================
echo   CredNest AI is now running!
echo ========================================
echo.
echo Backend: http://localhost:5000
echo Frontend: Opened in browser
echo.
echo Press any key to stop the server...
pause >nul

REM Stop the backend server
taskkill /FI "WINDOWTITLE eq CredNest AI - Backend*" /T /F >nul 2>&1

echo.
echo Server stopped. Goodbye!
timeout /t 2 /nobreak >nul
