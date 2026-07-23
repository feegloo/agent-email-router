from pydantic_ai import Agent

agent = Agent(
    model="ollama:qwen3:0.6b",
    instructions="Odpowiedz jednym zdaniem"
)

async def process_message(message: str) -> str:
    result = await agent.run(message)

    return result.output
