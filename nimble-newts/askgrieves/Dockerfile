FROM python:3.8.5-buster
COPY . /app
WORKDIR /app
RUN ["pip", "install", "pipenv"]
RUN ["pipenv", "install", "--system", "--deploy", "--ignore-pipfile"]
RUN ["python", "manage.py", "makemigrations"]
RUN ["python", "manage.py", "migrate"]
RUN ["python", "manage.py", "collectstatic"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "askgrieves.wsgi"]
