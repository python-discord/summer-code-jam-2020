#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $PG_HOST $PG_PORT; do
      sleep 1.0
    done

    echo "PostgreSQL started"
fi

python manage.py collectstatic --no-input
python manage.py migrate


exec "$@"