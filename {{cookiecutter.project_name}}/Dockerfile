FROM --platform=linux/amd64 python:{{cookiecutter.python_version}}-slim-bullseye AS build-main
RUN apt-get update --fix-missing && \
    apt-get install -y build-essential

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Install uv and setup venv
RUN pip install uv
RUN python -m venv --copies $VIRTUAL_ENV

# Take requirements and install them
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

FROM --platform=linux/amd64 python:{{cookiecutter.python_version}}-slim-bullseye AS runtime
COPY --from=build-main /venv /venv
RUN apt-get update --fix-missing && \
    apt-get install -y apt-transport-https wget icu-devtools
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
SHELL ["/bin/bash", "-c"]
RUN pip install --upgrade setuptools
WORKDIR /{{cookiecutter.project_name}}/app
COPY ./app /{{cookiecutter.project_name}}/app
COPY ./pyproject.toml /{{cookiecutter.project_name}}


FROM runtime AS main
CMD python main.py


FROM build-main AS build-tests
RUN uv sync --group tests --no-dev


FROM runtime AS tests
COPY --from=build-tests /venv /venv
COPY ./tests /{{cookiecutter.project_name}}/tests
WORKDIR /{{cookiecutter.project_name}}
CMD pytest -v --junitxml=reports/results.xml --cov-report=xml:reports/coverage.xml --cov=.


FROM build-main AS build-local
RUN uv sync --group dev,tests


FROM runtime AS local
COPY --from=build-local /venv /venv
CMD python main.py
