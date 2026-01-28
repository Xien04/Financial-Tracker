from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    APP_NAME: str = Field(default="Financial Tracker")
    DATABASE_URL: str = Field(default="sqlite:///./data.db")

    class Config:
        env_file = ".env"


settings = Settings()
