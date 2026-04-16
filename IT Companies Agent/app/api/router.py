"""Central router registry.

Keeping route registration in one place makes the API surface easy to audit.
"""

from fastapi import APIRouter

from app.api.routes.debug import router as debug_router
from app.api.routes.health import router as health_router
from app.api.routes.ingest import router as ingest_router
from app.api.routes.query import router as query_router
from app.api.routes.tickets import router as tickets_router
from app.api.routes.webhook import router as webhook_router
from app.api.routes.repositories import router as repositories_router
from app.api.routes.auth_debug import router as auth_debug_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(query_router)
api_router.include_router(ingest_router)
api_router.include_router(webhook_router)
api_router.include_router(debug_router)
api_router.include_router(tickets_router)
api_router.include_router(repositories_router)
api_router.include_router(auth_debug_router)

