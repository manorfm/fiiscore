# FROM python:3.10.9-alpine

# RUN apk update && apk upgrade --no-cache 

#  # python
# ENV PYTHONUNBUFFERED=1 \
#     # prevents python creating .pyc files
#     PYTHONDONTWRITEBYTECODE=1 \
#     \
#     # pip
#     PIP_NO_CACHE_DIR=off \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_DEFAULT_TIMEOUT=100 \
#     \
#     # poetry
#     # https://python-poetry.org/docs/configuration/#using-environment-variables
#     POETRY_VERSION=1.0.3 \
#     # make poetry install to this location
#     POETRY_HOME="/opt/poetry" \
#     # make poetry create the virtual environment in the project's root
#     # it gets named `.venv`
#     POETRY_VIRTUALENVS_IN_PROJECT=true \
#     # do not ask any interactive question
#     POETRY_NO_INTERACTION=1 \
#     \
#     # paths
#     # this is where our requirements + virtual environment will live
#     PYSETUP_PATH="/opt/pysetup" \
#     VENV_PATH="/opt/pysetup/.venv"

# RUN pip install poetry

# WORKDIR $PYSETUP_PATH
# COPY pyproject.toml ./
# RUN poetry install --only main

# # prepend poetry and venv to path
# ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# WORKDIR /app
# COPY /src ./src
# COPY app.py ./

# EXPOSE 3000

# CMD ["uvicorn", "app:app", "--reload", "--host","0.0.0.0", "--port", "8000"]

##----------------------------------------------------------------------------------------------------------------
FROM python:3.10.9-slim as python-base

    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.0.3 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# `builder-base` stage is used to build deps + create our virtual environment
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        #curl \
        # deps for building python deps
        build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN pip install poetry

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --only main


# `production` image used for runtime
FROM python-base as production
ENV FASTAPI_ENV=production
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
ADD src /app/src/
ADD app.py /app/
EXPOSE 8000

WORKDIR /app

CMD ["uvicorn", "app:app", "--reload", "--host","0.0.0.0"]

