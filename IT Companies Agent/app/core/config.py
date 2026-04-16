"""Application settings.

Loads environment variables from the .env file (if present) using
python-dotenv, then falls back to OS-level environment variables.
Never hard-code secrets here — put them in .env instead.
"""

from functools import lru_cache
from os import getenv

from dotenv import load_dotenv

# .env file root directory se load hogi
load_dotenv()


class Settings:
    project_name: str = getenv("DEVPULE_PROJECT_NAME", "DevPulse AI")
    project_version: str = getenv("DEVPULE_PROJECT_VERSION", "0.1.0")
    api_prefix: str = getenv("DEVPULE_API_PREFIX", "/api/v1")
    database_url: str = getenv(
        "DATABASE_URL",
        "sqlite+aiosqlite:///./devpulse.db"
    )
    jwt_secret: str | None = getenv("DEVPULE_JWT_SECRET")
    ag_api_key: str | None = getenv("AG_API_KEY")
    google_model: str = getenv("DEVPULE_GOOGLE_MODEL", "gemini-1.5-flash")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


