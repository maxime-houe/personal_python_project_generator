{% if cookiecutter.use_mongo == 'y' -%}
from pytest import fixture

from clients import Mongo


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
