import os

mongo_files = ["scripts/dump_db.sh", "scripts/mongo-init.js", "app/clients.py", "tests/clients_test.py"]
REMOVE_MONGO_PATHS = [
    '{% if cookiecutter.add_mongo_support != "y" %}' + file + '{% endif %}'
    for file in mongo_files
]

for path in REMOVE_MONGO_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)


docker_files = [
    "docker-compose.yml",
    "docker-compose.tests.yml",
    "Dockerfile",
    ".run/docker-compose.run.xml",
    ".run/docker-compose tests.run.xml",
    ".dockerignore",
]

REMOVE_DOCKER_PATHS = [
    '{% if cookiecutter.add_docker_support != "y" %}' + file + '{% endif %}'
    for file in docker_files
]

for path in REMOVE_DOCKER_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
