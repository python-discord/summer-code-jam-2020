FROM python:3.8-slim-buster 
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN rm -rf /code/*
COPY . /code/
RUN cat /code/.env
RUN apt-get update && apt-get install -y
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*
RUN pip install pipenv
COPY ./Pipfile* /code/
RUN pipenv install