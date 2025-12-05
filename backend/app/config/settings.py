from pydantic import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    APP_NAME: str = "Signalytic Backend"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Setting()