FROM python:3.9.16-alpine

RUN apk update
RUN apk add curl gcc

ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
  cd /usr/local/bin && \
  ln -s /opt/poetry/bin/poetry && \
  poetry config virtualenvs.create false

WORKDIR /app
COPY . .

RUN poetry install

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
