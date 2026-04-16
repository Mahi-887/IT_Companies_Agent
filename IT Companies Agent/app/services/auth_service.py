"""Supabase auth boundary.

This file stays small because the real implementation should be isolated from
the rest of the backend contract.
"""

from app.core.security import AuthContext


class AuthService:
    def verify_token(self, token: str) -> AuthContext:
        return AuthContext(user_id="demo-user", email="demo@example.com")

