# from docker hub https://hub.docker.com/_/python
FROM python:3.8-buster
# spit python logs to stdout
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
RUN python manage.py migrate