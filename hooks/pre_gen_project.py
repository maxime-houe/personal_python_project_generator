import re
import sys

# PROJECT NAME CHECK
PROJECT_NAME_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_name = "{{ cookiecutter.project_name }}"

if not re.match(PROJECT_NAME_REGEX, project_name):
    print("ERROR: %s is not a valid project name!" % project_name)

    # exits with status 1 to indicate failure
    sys.exit(1)

# PYTHON VERSION CHECK
PYTHON_VERSION_REGEX = r"^3\.([6-9]|1[0-9])$"
python_version = "{{ cookiecutter.python_version }}"

if not re.match(PYTHON_VERSION_REGEX, python_version):
    print("ERROR: %s is not a valid Python version!" % python_version)

    # exits with status 1 to indicate failure
    sys.exit(1)
