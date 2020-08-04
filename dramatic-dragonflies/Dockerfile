FROM i386/python:3.8-buster

STOPSIGNAL SIGQUIT
ENV PIP_NO_CACHE_DIR=false \
    PIPENV_HIDE_EMOJIS=1 \
    PIPENV_NOSPIN=1

ENTRYPOINT ["python"]
CMD ["manage.py", "run"]

RUN pip install -U pipenv

WORKDIR /app
COPY Pipfile*  terminal/term_handler.c ./
RUN mkdir -p ../build/
COPY package.json package-lock.json ../build/
RUN pipenv install --system --deploy

RUN apt-get -y update \
    && apt-get install -y \
    npm=5.8.* \
    gcc \
    #vim just for testing the terminal, we should remove it later
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && npm install --prefix ../build/ \
    && gcc -o ../build/process_watch term_handler.c -O3 -Wall -Wextra -lutil\
    && apt-get --purge -y autoremove npm gcc

COPY . .
