{% if cookiecutter.add_mongo_support == 'y' -%}
from clients import Mongo
from pytest import fixture


@fixture(scope="session")
def mongo():
    mongo = Mongo()
    return mongo


@fixture(scope="function", autouse=True)
def clean_database(mongo):
    mongo.client.drop_database("dev")
    yield None


@fixture(scope="function", autouse=True)
def reset_mongo(monkeypatch):
    monkeypatch.setattr(Mongo, "_instance", None)
{% endif %}