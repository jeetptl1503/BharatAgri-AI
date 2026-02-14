"""
BharatAgri AI — FastAPI Application Entry Point
API-only mode for Vercel serverless deployment.
Also serves frontend locally when not on Vercel.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models.database import create_tables
from app.routes import auth, predict, chatbot, reference
import os

IS_VERCEL = os.environ.get("VERCEL", False)

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

# Include API routers
app.include_router(auth.router)
app.include_router(predict.router)
app.include_router(chatbot.router)
app.include_router(reference.router)


@app.on_event("startup")
def startup():
    create_tables()


@app.get("/health")
def health():
    return {"status": "healthy", "platform": "vercel" if IS_VERCEL else "local"}


# Serve static frontend only when running locally (not on Vercel)
if not IS_VERCEL:
    FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")

    if os.path.exists(FRONTEND_DIR):
        app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

        @app.get("/")
        async def serve_index():
            return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

        @app.get("/{path:path}")
        async def serve_frontend(path: str):
            if path.startswith("api/") or path in ("docs", "redoc", "openapi.json", "health"):
                return None
            file_path = os.path.join(FRONTEND_DIR, path)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                return FileResponse(file_path)
            return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

