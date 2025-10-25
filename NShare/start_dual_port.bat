@echo off
REM Startup script for NShare with dual-port hosting
REM Port 8000: Read-Write access (for teacher)
REM Port 5555: Read-Only access (for students)

setlocal

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

REM Add the NShare directory to Python path
if defined PYTHONPATH (
    set "PYTHONPATH=%SCRIPT_DIR%;%PYTHONPATH%"
) else (
    set "PYTHONPATH=%SCRIPT_DIR%"
)

REM Create persistent data directory in user's home
set "DATA_DIR=%USERPROFILE%\.nshare_data\files"
if not exist "%DATA_DIR%" (
    mkdir "%DATA_DIR%"
)

echo Starting NShare with dual-port configuration...
echo Port 8000: Read-Write (Teacher)
echo Port 5555: Read-Only (Students)
echo Data directory: %DATA_DIR%
echo.

python "%SCRIPT_DIR%\scripts\run_server.py" ^
    --port 8000 ^
    --readonly-port 5555 ^
    --root "%DATA_DIR%" ^
    --verbose

REM Alternative with authentication token:
REM python "%SCRIPT_DIR%\scripts\run_server.py" ^
REM     --port 8000 ^
REM     --readonly-port 5555 ^
REM     --root "%DATA_DIR%" ^
REM     --auth-token "your-secret-token" ^
REM     --verbose

endlocal
