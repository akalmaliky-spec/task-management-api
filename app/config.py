"""Application settings, read from environment variables."""

import os

DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")
SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-only-insecure-key-change-me")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
CORS_ORIGINS: list[str] = [
    o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",") if o.strip()
]

if ENVIRONMENT == "production" and SECRET_KEY.startswith("dev-only"):
    raise RuntimeError("SECRET_KEY must be set in production")
