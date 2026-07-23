from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # load configuration from .env file during development (without container)
    model_config = SettingsConfigDict(env_file=".env")

    smtp_host: str
    smtp_port: int
    email_from: str
    email_human_resources: str
    email_help_desk: str
    email_it: str
    email_kadry: str
    email_other: str

settings = Settings() # type: ignore[call-arg]