FROM i386/python:3.8-buster

STOPSIGNAL SIGQUIT
ENV PIP_NO_CACHE_DIR=false \
    PIPENV_HIDE_EMOJIS=1 \
    PIPENV_NOSPIN=1

ENTRYPOINT ["python"]
CMD ["manage.py", "run"]

RUN apt-get -y update \
    && apt-get install -y \
        npm=5.8.* \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -U pipenv

WORKDIR /app
COPY Pipfile* package.json ./

RUN npm install && apt-get --purge -y autoremove npm
RUN pipenv install --system --deploy

COPY . .
