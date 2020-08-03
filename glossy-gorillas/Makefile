verify:
	poetry install
	poetry shell
	pytest

reset_db:
	poetry run ./manage.py flush --no-input
	poetry run ./manage.py migrate
	poetry run ./manage.py create_sample_db