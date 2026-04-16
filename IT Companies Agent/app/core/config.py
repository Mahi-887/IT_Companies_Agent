"""Application settings.

The settings object is intentionally small for now so environment handling
stays obvious and safe.
"""

from functools import lru_cache
from os import getenv


class Settings:
    project_name = getenv("DEVPULE_PROJECT_NAME", "DevPulse AI")
    project_version = getenv("DEVPULE_PROJECT_VERSION", "0.1.0")
    api_prefix = getenv("DEVPULE_API_PREFIX", "/api/v1")
    database_url = getenv(
        "DATABASE_URL", 
        "sqlite+aiosqlite:///./devpulse.db"
    )
    jwt_secret = getenv("DEVPULE_JWT_SECRET")
    ag_api_key = getenv("AG_API_KEY")
    google_model = getenv("DEVPULE_GOOGLE_MODEL", "gemini-1.5-flash")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

