import re
import logging

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from config import get_settings


logger = logging.getLogger(__name__)


class Mongo:
    _instance = None
    client: MongoClient = None
    # TODO: update the initialization of the database according to your project
    main: Database = None

    # Main
    tags: Collection = None

    def __new__(cls):
        if cls._instance is None:
            logger.info("🌿🌟 Creating new Mongo instance")
            cls._instance = super().__new__(cls)
            raw_url = get_settings().mongo_db_url
            cleaned_url = cls.parse_url(raw_url) + "/" + cls.retrieve_main_db()
            cls.client = MongoClient(cleaned_url)

            # Define Database instances
            cls.main = cls.client[f"{cls.retrieve_main_db()}"]

            # Define collections
            ## Main
            cls.reminders2 = cls.main.reminders2
            cls.tags = cls.main.tags
            cls.viks = cls.main.viks

        return cls._instance

    @staticmethod
    def parse_url(url: str) -> str:
        """
        Parse the url to remove the database name and the authentication

        Args:
            url (str): The url to parse

        Returns:
            str: The parsed url
        """
        regex_long = "((?P<base>.*://.*@.*)(/.*[?].*))"
        regex_medium = "((?P<base>.*://.*@.*)([/|?].*))"
        regex_short = "(?P<base>.*://.*@.*)"

        long_match = re.match(regex_long, url)
        medium_match = re.match(regex_medium, url)
        short_match = re.match(regex_short, url)

        if long_match:
            parsed_url = long_match.groupdict()["base"]
        elif medium_match:
            parsed_url = medium_match.groupdict()["base"]
        elif short_match:
            parsed_url = short_match.groupdict()["base"]
        else:
            logger.warning("🌿⚠️ Can't parse url")
            parsed_url = "mongodb://test:test@mongo:27017"

        cleaned_url = parsed_url

        return cleaned_url

    @staticmethod
    def retrieve_main_db() -> str:
        """
        Retrieve the main database name based on the stage.

        - If the stage is prod, use the prod database
        - If the stage is stage, use the beta database
        - If the stage is dev, use the dev database
        - If the stage is test, use the dev database
        - If the stage is anything else, use the dev database

        Returns:
            str: The name of the main database
        """
        test_env = ["tests", "test"]
        dev_env = ["dev", "development"]
        stage_env = ["stage", "beta"]
        prod_env = ["prod", "production"]

        if get_settings().stage in prod_env:
            main_db = "prod"
        elif get_settings().stage in stage_env:
            main_db = "beta"
        elif get_settings().stage in dev_env:
            main_db = "dev"
        elif get_settings().stage in test_env:
            main_db = "dev"
        else:
            main_db = get_settings().main_mongo_database

        return main_db
