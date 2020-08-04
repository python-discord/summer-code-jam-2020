up postgres :
	docker-compose up postgres
down:
	docker-compose down

venv:
	python3 -m venv venv

run:
	python friendly_frogs/manage.py runserver

migrate:
	python friendly_frogs/manage.py makemigrations
	python friendly_frogs/manage.py migrate

packages:
	pip install pipenv;pipenv install
