FROM python:3.11

WORKDIR /code

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock

RUN poetry install

COPY . /code
CMD ["poetry", "run", "fastapi", "run", "app", "--port", "80"]