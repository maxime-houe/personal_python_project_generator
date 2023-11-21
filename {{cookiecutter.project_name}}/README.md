{{cookiecutter.project_name}}
===========================

## Description
{{cookiecutter.description}}

## Specifications
* Python version > Python {{cookiecutter.python_version}}
* Poetry {{cookiecutter.poetry_version}}

## How to run the project

## Contributors
Run the following command to link the git hooks to your local git repository:
```bash
ln -s ../../hooks/pre-commit .git/hooks/pre-commit
ln -s ../../hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push
```
You also should install dev dependencies with the following command:
```bash
poetry install --with dev
```
Then, before each commit, you should run 
```bash
black .
```
This will format the python files accordingly. If not done, the hook will failed.