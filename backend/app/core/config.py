from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "NavTrace"
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/navtrace"

settings = Settings()