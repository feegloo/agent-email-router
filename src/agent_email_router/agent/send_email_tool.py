from typing import Literal

from pydantic_ai import RunContext

from agent_email_router.config import settings
from agent_email_router.services.email_service import send_email
from agent_email_router.agent.context import MessageContext

Department = Literal[
    "human_resources",
    "help_desk",
    "it",
    "kadry",
    "other"
]

def send_email_tool(
    ctx: RunContext[MessageContext],
    department: Department
 ) -> None:
    if ctx.deps.email_sent:
        # email already sent, do not call this tool again
        return

    print(f"Sending email to {department} department...")
    
    department_emails = {
        "human_resources": settings.email_human_resources,
        "help_desk": settings.email_help_desk,
        "it": settings.email_it,
        "kadry": settings.email_kadry,
        "other": settings.email_other,
    }

    send_email(
        to=department_emails[department],
        reply_to=ctx.deps.email,
        subject=f"New message from user '{ctx.deps.email}'",
        body=ctx.deps.message,
    )

    ctx.deps.email_sent = True

    print(f"Email sent to {department}")
