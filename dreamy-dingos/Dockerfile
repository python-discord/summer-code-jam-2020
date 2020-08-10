FROM python:3.8-slim-buster

RUN apt update
RUN apt install -y build-essential

RUN mkdir /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]