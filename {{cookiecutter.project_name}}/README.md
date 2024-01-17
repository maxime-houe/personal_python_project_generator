{{cookiecutter.project_name}}
===========================

## Description
{{cookiecutter.description}}

## How to run the project

## Contributors
### Setup
#### Git hooks
Run the following command to link the git hooks to your local git repository:
```bash
ln -s ../../hooks/pre-commit .git/hooks/pre-commit
ln -s ../../hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push
```
#### Dev dependencies
You also should install dev dependencies with the following command:
```bash
poetry install --with dev --no-root
```
### Contributing
#### Code formatting
Black library is used to format the code for this project.
Before each commit, you should run 
```bash
black .
```
This will format the python files accordingly. If not done, the pre-commit hook will fail.
#### Commit message
The project follows the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) convention.
Please follow the convention when you write your commit message.
