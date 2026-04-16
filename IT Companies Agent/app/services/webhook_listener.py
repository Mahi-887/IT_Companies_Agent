"""GitHub webhook handling."""

from dataclasses import dataclass

from app.schemas.webhook import GitHubWebhookEvent


@dataclass(slots=True)
class WebhookResult:
    event_type: str
    repo_id: str
    status: str
    next_step: str


class WebhookListener:
    def handle(self, event: GitHubWebhookEvent) -> WebhookResult:
        return WebhookResult(
            event_type=event.event_type,
            repo_id=event.repo_id,
            status="accepted",
            next_step="trigger_document_refresh",
        )

