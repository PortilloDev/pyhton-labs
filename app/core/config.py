from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Clean Architecture"
    environment: str = "local"
    debug: bool = True
    
settings = Settings()