FROM python:3.12

WORKDIR /drf_hw

COPY pyproject.toml .

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

COPY . .
