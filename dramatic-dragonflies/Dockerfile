FROM python:3.8-slim

STOPSIGNAL SIGQUIT
ENV PIP_NO_CACHE_DIR=false \
    PIPENV_HIDE_EMOJIS=1 \
    PIPENV_NOSPIN=1

ENTRYPOINT ["python"]
CMD ["manage.py", "run"]

RUN pip install -U pipenv

WORKDIR /app
COPY Pipfile* ./
RUN pipenv install --system --deploy

COPY . .
