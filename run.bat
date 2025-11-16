@echo off
echo ====================================
echo    Tool Dich Thuat - Starting...
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.7 or higher.
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting web server...
echo Open your browser at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause

