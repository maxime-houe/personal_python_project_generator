import os
import shutil

mongo_files = [
    "scripts/dump_db.sh",
    "scripts/mongo-init.js",
    "app/clients.py",
    "tests/clients_test.py",
]

docker_files = [
    "docker-compose.yml",
    "docker-compose.tests.yml",
    "Dockerfile",
    ".run/docker-compose.run.xml",
    ".run/docker-compose tests.run.xml",
    ".dockerignore",
]


def remove_paths(paths):
    for path in paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)


# Get user choices from environment variables set by Cookiecutter
add_mongo = os.environ.get("COOKIECUTTER_ADD_MONGO_SUPPORT", "n")
add_docker = os.environ.get("COOKIECUTTER_ADD_DOCKER_SUPPORT", "n")

if add_mongo.lower() != "y":
    remove_paths(mongo_files)

if add_docker.lower() != "y":
    remove_paths(docker_files)
