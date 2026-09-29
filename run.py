#!/usr/bin/env python3
"""
PocketSmart AI Server Runner
"""
import uvicorn

if __name__ == "__main__":
    print("==========================================================")
    print(">> Starting PocketSmart AI Server")
    print(">> Localhost:    http://localhost:8000")
    print(">> Loopback:     http://127.0.0.1:8000")
    print(">> Local LAN:    http://10.114.41.225:8000")
    print(">> Demo Account: demo@pocketsmart.ai | password123")
    print("==========================================================")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
