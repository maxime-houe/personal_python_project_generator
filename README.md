# Cookicutter template for Python project.

## Description
Personal template with poetry, docker, semantic-release github workflow.

## How to run the project
- Poetry is installed.
- At the root of this project, run the command
```bash
uv sync
```
- Run the command
```bash
cd ..
cookiecutter personal_python_project_generator
uv lock
```
And follow the instructions.

- Initialize git repository if wanted
```bash
git init
```