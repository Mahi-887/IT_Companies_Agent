"""Ticket suggestion service."""

from dataclasses import dataclass

from app.schemas.ticket import TicketSuggestionRequest


@dataclass(slots=True)
class TicketSuggestionResult:
    repo_id: str
    suggested_modules: list[str]
    suggested_owner: str


class TicketService:
    def suggest(self, request: TicketSuggestionRequest) -> TicketSuggestionResult:
        return TicketSuggestionResult(
            repo_id=request.repo_id,
            suggested_modules=["auth_service", "rag_query_service"],
            suggested_owner="unassigned",
        )

