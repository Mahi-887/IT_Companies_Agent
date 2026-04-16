from fastapi import APIRouter
from os import getenv
from app.core.security import generate_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/demo-token")
def get_demo_token():
    # Gated for safety as per kluster review P2.1
    if getenv("ENV") != "development":
        return {"error": "Endpoint only available in development mode"}
        
    token = generate_token("user_123", "dev@example.com")
    return {"token": token}
