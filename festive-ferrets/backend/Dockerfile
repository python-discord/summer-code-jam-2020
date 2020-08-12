FROM python:3.8

WORKDIR /usr/src/app

RUN apt update \
    && apt install -y python3-dev libpq-dev postgresql postgresql-contrib gcc musl-dev netcat

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]