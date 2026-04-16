"""FastAPI application entry point.

The app is assembled from small routers so the backend architecture stays
readable as the project grows.
"""

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()
    app = FastAPI(
        title=settings.project_name,
        version=settings.project_version,
        description="Modular monolith backend for DevPulse AI",
    )
    app.include_router(api_router, prefix=settings.api_prefix)
    return app


app = create_app()

