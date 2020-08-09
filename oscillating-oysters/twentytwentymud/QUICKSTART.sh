#!/bin/bash
docker-compose run --rm web python manage.py migrate
./load_data.sh
docker-compose up
