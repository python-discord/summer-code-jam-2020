FROM python
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY arena/ /code/
WORKDIR /code/arena
RUN python3 manage.py collectstatic
RUN python3 manage.py migrate
