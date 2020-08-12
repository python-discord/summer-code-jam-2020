#!/bin/bash
docker-compose run --rm web python manage.py loaddata MUD user
