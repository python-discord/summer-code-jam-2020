# Wily Wolves
This is the default README of your team's project. Please replace this by a README with more information on your project. At the very least, your README should contain information on how to set-up and run your project.

## Setup

This require Docker to be installed on your system.

While in the `wily-wolves` directory, run the following commands:

* `docker-compose up --detatch`
* `docker exec -it wily-wolves_mud_1 python mud/manage.py createsuperuser` and follow instructions.

Then head to `localhost:8000/mud` to access the game.
