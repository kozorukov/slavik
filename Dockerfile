FROM python:3.9.6

WORKDIR /opt/app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 80
