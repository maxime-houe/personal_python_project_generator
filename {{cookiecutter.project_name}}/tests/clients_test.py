from unittest.mock import MagicMock

from hypothesis import given
from hypothesis.strategies import text
from pytest import mark

from clients import Mongo


# Mongo Tests
class TestMongoParseUrl:
    @mark.unit
    @given(
        user_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz.-",
            min_size=5,
        ),
        password=text(
            alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            min_size=10,
        ),
        connection_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz.-",
            min_size=5,
        ),
    )
    def test_basic_url(
        self,
        user_name,
        password,
        connection_name,
    ):
        # Arrange
        ## Params
        database_url = f"mongodb://{user_name}:{password}@{connection_name}"

        # Act
        result = Mongo.parse_url(database_url)

        # Assert
        assert result == f"mongodb://{user_name}:{password}@{connection_name}"

    @mark.unit
    @given(
        user_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz.-",
            min_size=5,
        ),
        password=text(
            alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            min_size=10,
        ),
        connection_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz.-",
            min_size=5,
        ),
        db_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz_",
            min_size=5,
        ),
    )
    def test_url_with_db_name(
        self,
        user_name,
        password,
        connection_name,
        db_name,
    ):
        # Arrange
        ## Params
        database_url = f"mongodb://{user_name}:{password}@{connection_name}/{db_name}"

        # Act
        result = Mongo.parse_url(database_url)

        # Assert
        assert result == f"mongodb://{user_name}:{password}@{connection_name}"

    @mark.unit
    @given(
        user_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz.-",
            min_size=4,
        ),
        password=text(
            alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            min_size=10,
        ),
        connection_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz.-",
            min_size=5,
        ),
        params=text(
            alphabet="abcdefghijklmnopqrstuvwxyz=&",
            min_size=5,
        ),
    )
    def test_url_with_query_params(
        self,
        user_name,
        password,
        connection_name,
        params,
    ):
        # Arrange
        ## Params
        database_url = f"mongodb://{user_name}:{password}@{connection_name}?{params}"

        # Act
        result = Mongo.parse_url(database_url)

        # Assert
        assert result == f"mongodb://{user_name}:{password}@{connection_name}"

    @mark.unit
    @given(
        user_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz.-",
            min_size=4,
        ),
        password=text(
            alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            min_size=10,
        ),
        connection_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz.-",
            min_size=5,
        ),
        db_name=text(
            alphabet="abcdefghijklmnopqrstuvwxyz",
            min_size=5,
        ),
        params=text(
            alphabet="abcdefghijklmnopqrstuvwxyz=&",
            min_size=5,
        ),
    )
    def test_url_with_db_name_and_query_params(
        self,
        user_name,
        password,
        connection_name,
        db_name,
        params,
    ):
        # Arrange
        ## Params
        database_url = (
            f"mongodb://{user_name}:{password}@{connection_name}/{db_name}?{params}"
        )

        # Act
        result = Mongo.parse_url(database_url)

        # Assert
        assert result == f"mongodb://{user_name}:{password}@{connection_name}"


class TestMongoRetrieveMainDb:
    @mark.unit
    @mark.parametrize(
        "stage, result",
        [
            ("prod", "prod"),
            ("stage", "beta"),
            ("dev", "dev"),
            ("test", "dev"),
            ("local", "dev"),
        ],
    )
    def test_every_environment(self, monkeypatch, stage, result):
        # Arrange
        settings = MagicMock()
        settings.stage = stage
        monkeypatch.setattr("clients.get_settings", lambda: settings)

        # Act
        result = Mongo.retrieve_main_db()

        # Assert
        assert result == result
