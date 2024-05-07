from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_DATABASE: str
    POSTGRRES_USER: str
    POSTGRES_PASSWORD: str
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

load_dotenv()
settings = Settings()