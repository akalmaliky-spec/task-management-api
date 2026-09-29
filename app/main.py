"""FastAPI application entrypoint."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__, models  # noqa: F401  (models registers tables on Base)
from app.config import CORS_ORIGINS
from app.database import Base, engine
from app.routers import auth, tasks, users


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    # Create tables on startup. Swap for Alembic migrations when the schema
    # starts changing in production.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Task Management API", version=__version__, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok", "version": __version__}
