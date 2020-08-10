FROM python:3.8

RUN mkdir /code
RUN mkdir /code/static

COPY . /code/

COPY requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

WORKDIR /code

EXPOSE 8000

CMD ls && python manage.py collectstatic && python manage.py migrate && exec daphne -b 0.0.0.0 -p 8000 code_jam.asgi:application
 