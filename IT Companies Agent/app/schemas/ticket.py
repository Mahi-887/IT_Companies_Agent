"""Schemas for ticket mapping and suggestions."""

from dataclasses import dataclass


@dataclass(slots=True)
class TicketSuggestionRequest:
    repo_id: str
    summary: str

