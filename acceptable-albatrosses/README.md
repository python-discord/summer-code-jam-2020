# Acceptable Albatrosses

TBA Description and demo

## Installation

1. Run `python3 -m pip install pipenv` to install pipenv which manages this project's dependencies.
2. `cd` into this directory.
3. Run `python3 -m pipenv install` to install core dependencies or `python3 -m pipenv install --dev`
   to install development dependencies in a virtual environment.
4. Add a `.env` file in this directory with the following testing environment variables:

```
DJANGO_SECRET_KEY=test-key
```

5. Add `"localhost"` to `ALLOWED_HOSTS` in `albatrosses_hub/albatrosses_hub/settings.py`:

```py
ALLOWED_HOSTS = ["albatrosses-hub.com", "localhost"]
```

## Usage

1. Run `python3 -m pipenv shell` to enter the virtual environment.
2. Run `python albatrosses_hub/manage.py runserver` to start the development server.
3. Navigate to `localhost:8000` in your browser.

## License

MIT

## Contributing guidelines

See CONTRIBUTING.md.

## Attribution

See NOTICE.md.
