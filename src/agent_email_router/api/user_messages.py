from fastapi import APIRouter
from pydantic import BaseModel

from agent_email_router.services.email_service import send_email
from agent_email_router.config import settings

class UserMessageRequest(BaseModel):
    email: str
    message: str

router = APIRouter()

@router.post("/api/v1/user-messages")
async def user_messages(user_message_request: UserMessageRequest):
    send_email(
        to=settings.email_other,
        reply_to=user_message_request.email,
        subject=f"New message from user: '{user_message_request.message[0:10]}' (...)",
        body=user_message_request.message
    )

    return {"message": "processed"}