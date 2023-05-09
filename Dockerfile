FROM python:3.9.16-alpine

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH /root/.poetry/bin:$PATH

WORKDIR /app
COPY . .

RUN poetry install

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
