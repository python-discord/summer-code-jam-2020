FROM python:3.8-slim-buster 
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./ /app/
RUN apt-get update && apt-get install -y
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*
RUN pip install pipenv
COPY ./Pipfile* /app/
RUN pipenv install 