from pydantic_ai import Agent, ModelSettings

from agent_email_router.agent.context import MessageContext
from agent_email_router.agent.send_email_tool import send_email_tool
from agent_email_router.config import settings

agent = Agent(
    model=f"ollama:{settings.ollama_model}",
    deps_type=MessageContext,
    tools=[send_email_tool],
    instructions="""
        Jesteś agentem przekierowującym wiadomości używając narzędzia send_email_tool.

        Przeanalizuj wiadomość użytkownika i wyślij ją do jednego działu.
        Użyj raz narzędzia send_email_tool, aby wysłać wiadomość i zakończ zadanie.
        send_email_tool przyjmuje tylko jeden argument - nazwę działu: 'human_resources', 'help_desk', 'it', 'kadry', 'other'
        Nie przekazuj do send_email_tool wiadomości użytkownika ani adresu e-mail, ponieważ są one już dostępne w kontekście.

        Nazwy działów i przykłady pasujących do nich wiadomości:

        - 'human_resources' - sprawy rekrutacyjne i pracownicze, np. "Chcę zgłosić problem z moim przełożonym"
        - 'help_desk' - wsparcie i problemy z działaniem oprogramowania, np. "Nie mogę znaleźć potrzebnej opcji w systemie"
        - 'it' - problemy techniczne ze sprzętem lub dostępem, np. "Nie działa mi komputer"
        - 'kadry' - urlopy, wynagrodzenia, umowy i dokumenty pracownicze, np. "Chciałbym zgłosić urlop"
        - 'other' - wiadomości niepasujące do żadnego z powyższych działów
    """,
)


async def process_message(email: str, message: str) -> str:
    result = await agent.run(
        message,
        deps=MessageContext(email=email, message=message, email_sent=False),
        model_settings=ModelSettings(temperature=0, thinking="low"),
    )

    return result.output
