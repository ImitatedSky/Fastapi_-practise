from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 當config 和 .env都有的時候，會以.env為主
    APP_NAME: str = "fastapi-config"
    APP_VERSION: str = "0.1.0"
    API_HOST: str = "http://127.0.0.1:8000"
    API_KEY: str = "123456"

    class Config:
        env_file = '.env'

settings = Settings()