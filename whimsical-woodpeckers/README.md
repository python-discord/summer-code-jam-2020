# Whimsical Woodpeckers
This is the default README of your team's project. Please replace this by a README with more information on your project. At the very least, your README should contain information on how to set-up and run your project.

# Setup

### Requirements
- Python 3.8
- Django 3.0
- Node 10 / NPM

### Generate a secret key to use with Django
```python
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```
### Include a .env file or set environment variables to the following
```
SECRET_KEY=YOUR-SECRET-KEY
DEBUG=False
```
Place .env in this directory (whimsical-woodpeckers/.env)
```shell
pipenv install
cd www
npm install
npm run build
cd ..
cd mysite
pipenv run python manage.py runserver
```
