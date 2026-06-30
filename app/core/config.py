from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    OPENAI_API_KEY: str

    QDRANT_URL: str
    QDRANT_COLLECTION: str

    EMBED_MODEL: str
    CHAT_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()