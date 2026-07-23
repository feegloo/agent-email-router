import smtplib
from email.message import EmailMessage

from agent_email_router.config import settings


def send_email(to: str, reply_to: str, subject: str, body: str) -> None:
    message = EmailMessage()

    message.add_header("From", settings.email_from)
    message.add_header("To", to)
    message.add_header("Reply-To", reply_to)
    message.add_header("Subject", subject)

    message.set_content(body)

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as smtp:
        smtp.send_message(message)