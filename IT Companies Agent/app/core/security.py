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
    # Use fallback only for dev if not set
    secret = settings.jwt_secret or "default_secret_that_should_be_changed"
    return jwt.encode(
        {"sub": user_id, "email": email},
        secret,
        algorithm="HS256"
    )

