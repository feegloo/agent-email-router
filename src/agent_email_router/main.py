from fastapi import FastAPI
from agent_email_router.api.health import router as health_router

app = FastAPI()

app.include_router(health_router)