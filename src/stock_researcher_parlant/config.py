from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Statics
    GEMINI_MODEL_NAME: str = "gemini-2.5-flash"
    GEMINI_THINKING_BUDGET: int = 200
    GEMINI_TEMPERATURE: float = 1.0

    # Secrets
    GEMINI_API_KEY: str
    TAVILY_API_KEY: str


settings = Settings()
