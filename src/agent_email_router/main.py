from fastapi import FastAPI

from agent_email_router.api.health import router as health_router
from agent_email_router.api.user_messages import router as user_messages_router

app = FastAPI(docs_url="/api/v1/docs")

app.include_router(health_router)
app.include_router(user_messages_router)
