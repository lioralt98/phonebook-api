from typing import Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #DATABASE
    POSTGRES_HOST: str
    POSTGRES_DATABASE: str
    POSTGRRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str
    POSTGRES_URL: Optional[str] = None
    
    def __init__(self, **kwrgs):
        super().__init__(**kwrgs)
        self.POSTGRES_URL = f"postgresql://{self.POSTGRRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}"
        
    
    #GENERAL
    DEFAULT_AREA_CODE: int
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

load_dotenv()
settings = Settings()