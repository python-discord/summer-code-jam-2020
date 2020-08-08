#!/bin/bash
docker-compose run --rm web python manage.py dumpdata MUD.Room --indent 2 > MUD/fixtures/room_data.json
