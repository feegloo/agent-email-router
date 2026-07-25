from typing import Annotated
from fastapi import APIRouter, BackgroundTasks, status
from pydantic import BaseModel, StringConstraints, EmailStr

from agent_email_router.agent.message_agent import process_message

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

class UserMessageRequest(BaseModel):
    email: EmailStr
    message: NonEmptyString

router = APIRouter()

@router.post("/api/v1/user-messages", status_code=status.HTTP_202_ACCEPTED)
async def user_messages(body: UserMessageRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        process_message,
        email=body.email,
        message=body.message,
    )


    return {"message": "processing"}