#!/bin/bash
docker-compose run --rm web python manage.py dumpdata MUD --indent 2 > MUD/fixtures/MUD.json
docker-compose run --rm web python manage.py dumpdata auth.user --indent 2 > MUD/fixtures/auth.user.json
