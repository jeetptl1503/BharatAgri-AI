from pydantic_settings import BaseSettings
import os

IS_VERCEL = os.environ.get("VERCEL", False)

class Settings(BaseSettings):
    SECRET_KEY: str = "bharatagri-dev-secret-key-2024"
    ADMIN_SECRET_KEY: str = "bharatagri-admin-2024"
    DATABASE_URL: str = "sqlite:////tmp/bharatagri.db" if IS_VERCEL else "sqlite:///./bharatagri.db"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()

