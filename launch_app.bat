@echo off
title Launcher

:: Request admin if needed
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Fix working directory (THIS is the important part)
cd /d "%~dp0"

echo Running as admin from correct directory...
python main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] The program crashed or stopped unexpectedly.
    pause
)