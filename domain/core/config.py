from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    SERVER_PORT: int
    SERVER_MODE: str
    SECRET_KEY: str
    ALGORITHM: str
    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()