import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    SECRET_KEY: str
    ALGORITHM: str
    JWT_SECRET_KEY: str
    JWT_LIFE_TIME: int
    COOKIE_MAX_AGE: str
    RESET_PASSWORD_SECRET_KEY: str
    RESET_PASSWORD_SECRET_KEY : str
    model_config = SettingsConfigDict(extra='allow',
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"))
    


settings = Settings()


def get_db_url():
    return (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@"
            f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")


def get_auth_data():
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}