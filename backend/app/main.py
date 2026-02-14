"""
BharatAgri AI — FastAPI Application Entry Point
Serves both API and frontend static files.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models.database import create_tables
from app.routes import auth, predict, chatbot, reference
import os

app = FastAPI(
    title="BharatAgri AI",
    description="Intelligent Crop & Yield Advisory System for Indian Agriculture",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers FIRST (before catch-all)
app.include_router(auth.router)
app.include_router(predict.router)
app.include_router(chatbot.router)
app.include_router(reference.router)


@app.on_event("startup")
def startup():
    create_tables()


@app.get("/health")
def health():
    return {"status": "healthy"}


# Serve static frontend LAST
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")

if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

    @app.get("/")
    async def serve_index():
        return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

    @app.get("/{path:path}")
    async def serve_frontend(path: str):
        # Don't catch API or docs routes
        if path.startswith("api/") or path in ("docs", "redoc", "openapi.json", "health"):
            return None
        # Try to serve the file directly
        file_path = os.path.join(FRONTEND_DIR, path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        # Fall back to index.html for SPA routing
        return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
