@echo off
title PocketSmart AI Server
cd /d "%~dp0"
echo ==========================================================
echo Starting PocketSmart AI Server...
echo Web Address: http://localhost:8000
echo ==========================================================
python run.py
pause
