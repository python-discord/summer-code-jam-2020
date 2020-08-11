setup:
	python3.8 get-poetry.py
	source $HOME/.poetry/env
	poetry install

verify:
	poetry check
	poetry run pytest

reset_db:
	rm db.sqlite3
	poetry run ./manage.py migrate
	poetry run ./manage.py create_sample_db