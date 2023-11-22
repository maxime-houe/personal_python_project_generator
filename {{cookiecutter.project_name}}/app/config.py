from functools import lru_cache
import logging

from pydantic_settings import BaseSettings


__version__ = "0.0.0"


class Settings(BaseSettings):
    project_name: str = "{{cookiecutter.project_name}}"
    version: str = __version__
    stage: str = "local"
    location: str = "local"
    environment: str = f"{stage}-{location}"
{% if cookiecutter.use_mongo == 'y' -%}

    # MongoDB
    mongo_url: str = "mongodb://test:test@localhost:27017/dev"
    main_mongo_database: str = "dev"
{% endif %}


def configure_log():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] - %(message)s",
        handlers=[
            logging.StreamHandler()  # Add a stream handler to log to the console
        ],
    )
    # # remove every other logger's handlers
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).setLevel(logging.WARNING)
        logging.getLogger(name).propagate = True


@lru_cache()
def get_settings():
    return Settings()
