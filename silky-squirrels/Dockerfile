FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install pipenv
COPY Pipfile.lock /code
COPY Pipfile /code
RUN pipenv install --deploy

COPY . /code/

CMD pipenv run python manage.py runserver 0.0.0.0:8000