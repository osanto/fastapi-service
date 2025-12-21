import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Render / production
    database_url: Optional[str] = None

    # Local / docker (optional)
    database_username: Optional[str] = None
    database_password: Optional[str] = None
    database_hostname: Optional[str] = None
    database_port: Optional[str] = None
    database_name: Optional[str] = None

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = os.getenv("ENV_FILE", ".env.local")
        env_file_encoding = "utf-8"


settings = Settings()
