from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(title="PaperGuard API", version="0.1.0")
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/api/health")
def health_check():
    return {"status": "ok", "phase": 1, "database": "mock"}


@app.get("/")
def serve_app():
    return FileResponse(FRONTEND_DIR / "index.html")

