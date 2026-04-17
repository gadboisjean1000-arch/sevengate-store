@echo off
chcp 65001 >nul
title OMEGAHUB - Simple Launcher

echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║          OMEGAHUB - THE OS OF THE AI ERA             ║
echo  ║          Finance Omega Active                           ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.

REM Check port 8081
netstat -ano 2>nul | findstr ":8081" | findstr "LISTENING" >nul
if %errorlevel%==0 (
    echo  ✅ API already running on port 8081
    goto :links
)

echo  ▶ Starting API Server...
start "OMEGAHUB API" cmd /c "cd /d %~dp0www\api && python api_server_simple.py"

echo  ▶ Waiting for API...
timeout /t 3 /nobreak >nul

:links
echo.
echo  ╔══════════════════════════════════════════════════════════╗
echo  ║                    ALL SYSTEMS ONLINE                    ║
echo  ╚══════════════════════════════════════════════════════════╝
echo.
echo  🌐 Local:    http://localhost:8081
echo  🌐 Health:   http://localhost:8081/health
echo  💬 Chat:     http://localhost:8081/api/chat
echo  📊 Market:   http://localhost:8081/api/finance/market
echo.
echo  Press any key to exit...
pause >nul
