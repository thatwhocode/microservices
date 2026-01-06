from shared_packages.core.config import  PostgresSettings

class Settings(PostgresSettings):
    PROJECT_NAME: str = "Chat service"
    ALGORITHM : str = "HS256"

settings = Settings()