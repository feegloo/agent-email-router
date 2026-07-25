from pydantic_ai import Agent, ModelSettings

from agent_email_router.agent.send_email_tool import send_email_tool
from agent_email_router.agent.context import MessageContext


agent = Agent(
    model="ollama:qwen3:0.6b",
    deps_type=MessageContext,
    tools=[send_email_tool],
    instructions="""
        Jesteś agentem odpowiedzialnym za przekierowywanie wiadomości.

        Przeanalizuj wiadomość użytkownika i wyślij ją dokładnie do jednego działu, używając narzędzia send_email_tool.
        Dopuszczalne wartości działów: 'human_resources', 'help_desk', 'it', 'kadry', 'other'

        Musisz użyć narzędzia send_email_tool, aby wysłać wiadomość.
        Wywołaj narzędzie dokładnie jeden raz.
        Po poprawnym wykonaniu narzędzia nie wywołuj żadnych kolejnych narzędzi i zakończ zadanie.
        send_email_tool przyjmuje od Ciebie tylko jeden argument: nazwa działu jako niepusty string.
        Nie przekazuj treści wiadomości, adresu email ani dodatkowych argumentów oprócz nazwy działu.
        
        Nazwy działów i przykłady wiadomości, które do nich pasują:

        - 'human_resources' - sprawy rekrutacyjne i pracownicze, np. "Chcę zgłosić problem z moim przełożonym"
        - 'help_desk' - wsparcie i problemy z działaniem oprogramowania, np. "Nie mogę znaleźć potrzebnej opcji w systemie"
        - 'it' - problemy techniczne ze sprzętem lub dostępem, np. "Nie działa mi komputer"
        - 'kadry' - urlopy, wynagrodzenia, umowy i dokumenty pracownicze, np. "Chciałbym zgłosić urlop"
        - 'other' - wiadomości niepasujące do żadnego z powyższych działów
    """
)


async def process_message(email: str, message: str) -> str:
    result = await agent.run(
        message,
        deps=MessageContext(
            email=email,
            message=message,
            email_sent=False
        ),
        model_settings=ModelSettings(
            temperature=0,
            thinking="low"
        )
    )

    return result.output 