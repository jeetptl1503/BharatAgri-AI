"""
Vercel Serverless Entry Point for BharatAgri AI.
Wraps the FastAPI app for Vercel's Python runtime.
"""
import sys
import os

# Add backend directory to Python path
backend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend")
sys.path.insert(0, backend_dir)

from app.main import app

# Vercel uses the `app` variable directly as the ASGI handler
