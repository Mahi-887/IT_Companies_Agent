"""Authentication and authorization helpers."""

from dataclasses import dataclass


import jwt
from app.core.config import get_settings

@dataclass(slots=True)
class AuthContext:
    user_id: str
    email: str
    role: str = "member"


class AuthorizationError(Exception):
    """Raised when access control validation fails."""

def generate_token(user_id: str, email: str) -> str:
    settings = get_settings()
    secret = settings.jwt_secret
    if not secret:
        raise ValueError(
            "DEVPULE_JWT_SECRET environment variable is not set. "
            "Set a strong random secret in your .env file."
        )
    return jwt.encode(
        {"sub": user_id, "email": email},
        secret,
        algorithm="HS256"
    )

