from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "{{cookiecutter.project_name}}"
    version: str = "0.1.0"
    stage: str = "local"
    location: str = "local"
    environment: str = f"{stage}-{location}"


@lru_cache()
def get_settings():
    return Settings()
