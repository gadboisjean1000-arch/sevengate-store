@echo off
REM OMEGAHUB - API Tunnel Launcher
REM Keeps the API publicly accessible

echo Starting OMEGAHUB API Tunnel...
echo.

REM Start API in background
start "OMEGAHUB API" python api_cloud.py

REM Wait for API to start
timeout /t 3 /nobreak > nul

REM Start tunnel (keeps running)
ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -o ServerAliveCountMax=3 -R 80:localhost:8081 3.208.46.244
