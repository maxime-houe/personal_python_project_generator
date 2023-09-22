{{cookiecutter.project_name}}
===========================

## Description
{{cookiecutter.description}}

## Specifications
* Python {{cookiecutter.python_version}}
* Poetry {{cookiecutter.poetry_version}}
{% if cookiecutter.use_mongo == 'y' -%}
* MongoDB
{% endif %}
## Documentation: