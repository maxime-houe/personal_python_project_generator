import os

mongo_files = ["scripts/dump_db.sh", "scripts/mongo-init.js", "app/clients.py", "tests/clients_test.py"]
REMOVE_MONGO_PATHS = [
    '{% if cookiecutter.use_mongo != "y" %}' + file + '{% endif %}'
    for file in mongo_files
]

for path in REMOVE_MONGO_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
