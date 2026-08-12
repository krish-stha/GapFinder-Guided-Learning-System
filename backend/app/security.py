"""
JWT issuance/verification. Pure token logic, no DB access - kept separate
from auth.py so the mastery-engine philosophy (pure functions, easy to unit
test) applies here too.

SECRET_KEY must be overridden via the JWT_SECRET_KEY env var for any
deployment beyond local dev - the fallback below is intentionally public.
"""
import os
from datetime import datetime, timedelta

import jwt

SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "dev-only-insecure-secret-set-JWT_SECRET_KEY-in-prod")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days


def create_access_token(student_id: int) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode({"sub": str(student_id), "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)


def decode_student_id(token: str) -> int:
    """Raises jwt.PyJWTError (expired/malformed/bad signature) on failure."""
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return int(payload["sub"])
