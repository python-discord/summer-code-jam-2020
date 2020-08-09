FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
WORKDIR /app/src
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["runserver", "0.0.0.0:8000"]