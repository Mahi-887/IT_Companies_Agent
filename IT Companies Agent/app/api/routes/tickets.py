"""Ticket suggestion and enrichment endpoints."""

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope
from app.schemas.ticket import TicketSuggestionRequest
from app.services.ticket_service import TicketService

router = APIRouter(tags=["tickets"])
ticket_service = TicketService()


@router.get("/tickets/suggestions", response_model=ApiEnvelope)
def ticket_suggestions(repo_id: str, summary: str = "") -> ApiEnvelope:
    request = TicketSuggestionRequest(repo_id=repo_id, summary=summary)
    result = ticket_service.suggest(request)
    return ApiEnvelope.success(message="Ticket suggestions ready", data=result)

