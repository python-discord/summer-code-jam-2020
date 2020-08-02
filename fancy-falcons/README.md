# Fancy Falcons

Setup info coming soon. Changed to enable opening a pull request.

# Setup guide (git pull and pipenv setup) - Ubuntu terminal
1. clone the repository _git clone https://github.com/nkesedre/summer-code-jam-2020.git_
2. go into our team folder _cd summer-code-jam-2020/fancy-falcons/_
3. make sure pipenv is installed _sudo apt-get install pipenv_
4. create pipenv environment for this project (within 'fancy-falcons' folder) _pipenv install_
5. start pipenv shell _pipenv shell_
6. If not already on master switch to the pipenv-setup branch _git checkout origin/pipenv-setup_
7. go to the django project folder _cd fancy-falcons-proj_
8. start the server _python3 manage.py runserver_
9. When you open the browser and go to _localhost:8000_ you should see a "Hello world!"
