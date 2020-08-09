# Fancy Falcons

The Earl(y) Internet, a community for people who have the title "Earl".

# Pipenv setup guide - Ubuntu terminal
1. Clone the repository _git clone https://github.com/python-discord/summer-code-jam-2020.git_ (skip this point if local copy already exists)
2. Go into our team folder _cd summer-code-jam-2020/fancy-falcons/_
3. Make sure pipenv is installed _sudo apt-get install pipenv_
4. Create pipenv environment for this project (within 'fancy-falcons' folder) _pipenv install_
5. Start pipenv shell _pipenv shell_
6. Go to the django project folder _cd fancy-falcons-proj_
7. Migrate: _python3 manage.py migrate --run-syncdb_
8. Start the server _python3 manage.py runserver_
9. Your good to go, open your browser an go to _localhost:8000_

# Pipenv setup guide - PyCharm

