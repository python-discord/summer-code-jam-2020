#!/bin/bash
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py loaddata MUD user
docker-compose up
