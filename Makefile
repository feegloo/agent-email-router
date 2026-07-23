dev:
	OLLAMA_BASE_URL=http://localhost:11434/v1 uvicorn agent_email_router.main:app --reload
