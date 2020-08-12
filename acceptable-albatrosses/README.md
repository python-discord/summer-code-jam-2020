# Acceptable Albatrosses

![logo][logo-url]

**Albatrosses Hub** is a fun website where you can spend your time discussing about something in the forum.

## Installation
1. Make sure u have git installed.
1. Make sure you have any version of python higher than 3.5 installed.
   1. You can run `python --version` or `python3 --version` to check if python is installed.
   1. If it is not installed head over to https://www.python.org/ and follow the tutorial and get the latest version of python.
1. Clone the repository and run `cd acceptable-albatrosses` to change directory into the acceptable-albatrosses folder. 
1. Run `pip3 install -r requirements.txt` which will install all the requirements for this project.
1. Another step that you will need for the project to run is creating the environment variables:
   1. For __Windows__ in command prompt: you can run `set DJANGO_SECRET_KEY=test-key` without any spaces near `=` sign.
   1. For __Linux__ in terminal:         you can run `export DJANGO_SECRET_KEY=test-key` without any spaces near `=` sign.

## How to Run

2. Run `python albatrosses_hub/manage.py runserver` to start the development server.
3. Navigate to `localhost:8000` in your browser.

## License

See [LICENSE][LICENSE-url]

## Contributing guidelines

See [CONTRIBUTING.md][CONTRIBUTE-url]

## Attribution

See [NOTICE.md][NOTICE-url]

[logo-url]: ./albatrosses_hub/home/static/albatrosses_hub/img/albatrosses-logo-small.png
[LICENSE-url]: ../LICENSE
[NOTICE-url]: ./NOTICE.md
[CONTRIBUTE-url]: ./CONTRIBUTING.md
