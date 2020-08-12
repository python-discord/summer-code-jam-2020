# Wily Wolves
This is our entry for the Summer Code Jam 2020! It is a Multi User Dungeon (MUD) framework where you can create your own map and (hopefully if we get to it) place NPCs to interact with. As the name suggests, multiple users can play on the same map at the same time and interact.

## Setup
This require Docker to be installed on your system.

While in the `wily-wolves` directory, run the following commands:

* `docker-compose up --detatch`
* `docker exec -it wily-wolves_mud_1 python mud/manage.py createsuperuser` and follow instructions.

Then head to `localhost:8000/mud` to access the game.

## How to use the framework and start a game

Once you have a superuser account created, you will be able log in to the administration panel. Once there, you will have to create ``Location``s to the game, especially the starting position ``(x=0, y=0, z=0)``, and any others you might want to add.

Once the map is done, you can go to the game page (``<the IP address>/mud``) and create a new user account with ``new username userpassword``, then enter the command ``start``. This will place you at the begining of the map (Location ``(x=0, y=0, z=0)``). Enter the ``help`` command to see the list of available commands.

