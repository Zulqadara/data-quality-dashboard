from pydantic import BaseSettings


class DBSettings(BaseSettings):
    DATABASE_URL: str
    class Config:
        env_file = ".env"

db_settings = DBSettings()