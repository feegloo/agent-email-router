from fastapi import APIRouter
from pydantic import BaseModel

from agent_email_router.services.email_service import send_email
from agent_email_router.config import settings

class UserMessageRequest(BaseModel):
    email: str
    message: str

router = APIRouter()

@router.post("/api/v1/user-messages")
def user_messages(userMessageRequest: UserMessageRequest):
    send_email(
        to=settings.email_other,
        reply_to=userMessageRequest.email,
        subject="User email",
        body=userMessageRequest.message
    )

    return {"message": "processed"}