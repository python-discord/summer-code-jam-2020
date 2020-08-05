FROM python:3.8

RUN mkdir /code

COPY . /code/

COPY requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

WORKDIR /code

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
 