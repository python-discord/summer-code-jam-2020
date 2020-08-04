# Mysterious Mice
This is the default README of your team's project. Please replace this by a README with more information on your project. At the very least, your README should contain information on how to set-up and run your project.

# Setting Up The Database
## Before Committing Changes
Create a JSON dump of the data in the database file by running `python manage.py dumpdata > db.json`

## After Cloning/Pulling From Repository
Verify the database file has the proper structure by running the following commands:  
`python manage.py makemigrations`  
`python manage.py migrate`

Then populate the database by running `python manage.py loaddata db.json`

# Running Spacebook
## Docker-Compose
Run `docker-compose build` to build the Docker image.

Run `docker-compose up -d` to build, create, start and attach the container. The `d` runs the container in the background.
