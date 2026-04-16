"""Webhook endpoints for GitHub events."""

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope
from app.schemas.webhook import GitHubWebhookEvent
from app.services.webhook_listener import WebhookListener

router = APIRouter(tags=["webhook"])
listener = WebhookListener()


@router.post("/webhook/github", response_model=ApiEnvelope)
def github_webhook(payload: GitHubWebhookEvent) -> ApiEnvelope:
    result = listener.handle(payload)
    return ApiEnvelope.success(message="Webhook accepted", data=result)

