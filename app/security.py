"""Password hashing and JWT helpers."""

from datetime import datetime, timedelta, timezone
from typing import Optional

import bcrypt
import jwt

from app.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


def create_access_token(subject: str, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    return jwt.encode({"sub": subject, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> Optional[str]:
    """Return the token subject (user email), or None if the token is invalid/expired."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        return None
    sub = payload.get("sub")
    return sub if isinstance(sub, str) else None
