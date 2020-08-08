![Spacebook Logo](spacebook-logo-light.png)

# Spacebook, by Mysterious Mice
Welcome to Spacebook, a social media site created for NASA's rovers on Mars! 

## Installation

### With Docker

In the main `mysterious-mice\` directory:
- Run `docker-compose build` to build the Docker image.
- Run `docker-compose up -d` to build, create, start and attach the container. The `d` runs the container in the background.

### Without Docker

In the main `mysterious-mice\` directory:
- Run `venv\Scripts\activate` to activate the virtual environment.
- Run `python -m pip install --upgrade pip` to ensure the latest version of pip is installed.
- Run `python -m pip install -r requirements.txt` to install all the required packages.

In the `spacebook\` subdirectory:
- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Run `python manage.py loaddata db.json`
- Run `python maange.py runserver`

## Updating The Database

If you made changes to the database that you want to commit, run `python manage.py dumpdata > db.json` in the `spacebook\` subdirectory to create a JSON file.

## Sources

All photos take on or of Mars are courtesy of NASA.  
The starry background image is courtesy of [1-background.com](https://1-background.com/stars_1.htm)
