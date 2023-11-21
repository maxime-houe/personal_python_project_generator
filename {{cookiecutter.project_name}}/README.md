{{cookiecutter.project_name}}
===========================

## Description
{{cookiecutter.description}}

## Specifications
* Python version > Python {{cookiecutter.python_version}}
* Poetry {{cookiecutter.poetry_version}}

## How to run the project

## Contributors
Run the following command to link the pre-commit hook to your local git repository:
```bash
ln -s ../../hooks/pre-commit .git/hooks/pre-commit
ln -s ../../hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push
```