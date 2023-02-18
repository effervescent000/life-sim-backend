from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    jwt_secret: str
    jwt_algo: str
    jwt_encryption: str

    class Config:
        env_file = ".env"


settings = Settings()
