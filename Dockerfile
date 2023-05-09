FROM python:3.9.16-alpine

RUN apk update
RUN apk add curl gcc

RUN python -m pip install --upgrade pip

ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
  cd /usr/local/bin && \
  ln -s /opt/poetry/bin/poetry && \
  poetry config virtualenvs.create false && \
  poetry config experimental.new-installer false

WORKDIR /app
COPY . .

RUN poetry install

CMD [ "python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
