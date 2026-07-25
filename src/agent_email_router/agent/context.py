from dataclasses import dataclass


@dataclass
class MessageContext:
    email: str
    message: str
    email_sent: bool = False