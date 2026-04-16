"""Dependency helpers for request-scoped services."""

from app.services.auth_service import AuthService
from app.services.repo_service import RepoService


def get_auth_service() -> AuthService:
    return AuthService()


def get_repo_service() -> RepoService:
    return RepoService()

import jwt
from fastapi import Header, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import AuthContext
from app.core.config import get_settings

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)) -> AuthContext:
    token = credentials.credentials
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        user_id = payload.get("sub")
        if not user_id:
            raise ValueError("No matching user ID in token sub claim")
        return AuthContext(user_id=user_id, email=payload.get("email", "dummy@example.com"))
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token payload")

