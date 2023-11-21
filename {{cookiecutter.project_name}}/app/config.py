from functools import lru_cache

from pydantic_settings import BaseSettings


__version__ = "0.0.0"


class Settings(BaseSettings):
    project_name: str = "{{cookiecutter.project_name}}"
    version: str = __version__
    stage: str = "local"
    location: str = "local"
    environment: str = f"{stage}-{location}"


@lru_cache()
def get_settings():
    return Settings()
