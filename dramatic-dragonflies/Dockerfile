FROM i386/debian:buster AS builder

RUN apt-get -y update       \
    && apt-get install -y   \
    gcc                 \
    git                 \
    libcap-dev          \
    make                \
    linux-headers-686   \
    wget

WORKDIR /minijail
RUN git clone                                    \
    --single-branch                          \
    --depth 1                                \
    https://github.com/google/minijail.git . \
    && make LIBDIR=/lib64



FROM i386/python:3.8-buster

STOPSIGNAL SIGQUIT
ENV PIP_NO_CACHE_DIR=false \
    PIPENV_HIDE_EMOJIS=1   \
    PIPENV_NOSPIN=1

ENTRYPOINT ["python"]
CMD ["manage.py", "run"]

COPY --from=builder /minijail/libminijail.so /minijail/libminijailpreload.so /lib64/
COPY --from=builder /minijail/minijail0 /usr/bin/
COPY rom.tar.gz /

RUN tar -xzf /rom.tar.gz && rm /rom.tar.gz

RUN pip install -U pipenv

WORKDIR /app
COPY Pipfile*  ./
RUN mkdir -p ../build/
COPY package.json package-lock.json ../build/
RUN pipenv install --system --deploy

RUN apt-get -y update \
    && apt-get install -y \
    npm=5.8.* \
    #vim just for testing the terminal, we should remove it later
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && npm install --prefix ../build/ \
    && apt-get --purge -y autoremove npm
COPY tools/process_watch.c ./
RUN  gcc -o ../build/process_watch process_watch.c -O3 -Wall -Wextra -lutil
COPY . .
