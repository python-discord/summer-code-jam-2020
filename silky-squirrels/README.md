# Silky Squirrels
This is the default README of your team's project. Please replace this by a README with more information on your project. At the very least, your README should contain information on how to set-up and run your project.

## Setup

### Requirements
- Docker
  - [Docker Desktop on Windows 10 Home](https://docs.docker.com/docker-for-windows/install-windows-home/#install-docker-desktop-on-windows-10-home)
- Python 3.8+ w/ Pip
- Pipenv (https://pipenv-fork.readthedocs.io/en/latest/)
  
  ```shell script
  pip install pipenv
  ```
  - Make sure `pipenv` is in your PATH environment variable so you can run `pipenv` commands below.
  
### Install Dependencies/Packages

```shell script
cd silky-squirrels/
pipenv install
```

### Run WebApp
 
```shell script
# Enter into virtual environment
pipenv shell

# Make Migrations
python manage.py migrate


# Open 2 Terminals (One for Each below)

# Run Docker Containers
docker-compose up

# Run server
python manage.py runserver
```
Original source from https://github.com/CoreyMSchafer/code_snippets CoreyMSchafer
