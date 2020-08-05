FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN pip install -U "pipenv==2018.11.26"

WORKDIR /app
COPY Pipfile* ./

RUN pipenv install --system --deploy

COPY cuddly_chameleons ./
