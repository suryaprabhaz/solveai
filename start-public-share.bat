@echo off
echo Starting SolveAI Public Tunnel...
echo.
echo ========================================================
echo Keeping this window open allows ANY laptop in the world
echo to access your Ollama model via SolveAI!
echo ========================================================
echo.
"C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://localhost:11434
pause
