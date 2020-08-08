FROM python:3.8
ENV PYTHONUNBUFFERED 1
ARG SECRET_KEY=foobarthisisforbuildonly
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY forumthing/. /app/
RUN python manage.py makemigrations
RUN python manage.py migrate
