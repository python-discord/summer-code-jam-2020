[![Team Logo](./horsescodejamlogo.png?raw=true "Logo")](#)  

<hr>

### Production Installation:
1. Clone master branch

2. Add domains/IPs to `settings.ALLOWED_HOSTS` if applicable

3. Copy/create prod.env into `/hysterical-horses'

4. Create Postgres database and specify database settings in prod.env file (or set django_debug to True to use a local
database for testing)

5. Navigate to `hysterical-horses/` and start docker container, could use `docker-compose up --build`

6. Navigate to project folder in Docker bash and run `python manage.py createsuperuser` and follow the prompts to create
an admin (admin account is also to be used for testing all feature without the need to slowly level up first)

7. Site will run at a default ip of `0.0.0.0:8000` and should be accessible though `http://127.0.0.1:8000/` on the 
machine.

### Development Installation:
1. Clone repository

2. Create virtual environment for this project ([virtualenv](https://pypi.org/project/virtualenv/))

3. Activate your virtual environment 

4. Navigate to /histerical-horses directory and `pip install -r requirements.txt`
 *this will install every required module for the project* 
 
5. (*only used if not using docker*) Create environment variable for Django secret key: search "environment variable" in windows search bar => 
edit the system environment variables => environment variables => user variables for "current user's name here" => new =>
variable name == summer_jam_secret_key, variable value == (use secret key that should be pinned in hysterical-horses chat)

6. run `python manage.py migrate` in order for the site to behave properly (the database
file will be ignored when committing to avoid merge conflicts)

7. (*optional in dev, required for full functionality*) create a file dev.env in `\hysterical-horses` and add `summer_jam_secret_key=INSERT_SECRET_KEY_HERE` run `docker-compose up --build` in `\hysterical-horses` to build dependencies, start redis, and start the server.
