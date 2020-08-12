FROM python:3.8-alpine
WORKDIR /app
COPY . ./
RUN pip3 install -r requirements.txt
WORKDIR /app/timescape
RUN python manage.py migrate
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]