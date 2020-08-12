# Lively Lions
 Text Based Game (PvP in ROOM)

# MUD


## Features

- backend - Django
- frontend - html (with xterm.js, ajax)

## Requirements
Requires python 3.8+ (with pip)

---
## To the team members

- [How to contribute to the code](https://github.com/lively-lions/summer-code-jam-2020/wiki)

---

## Setup (for development)
To prepare for development, run commands (from this directory):

```
python3 --version
> Python 3.8.X

cd summer-code-jam-2020/lively-lions
(python3 -m) pip install pipenv
mkdir .venv
(python3 -m) pipenv install --dev
(python3 -m) pipenv run pre-commit install
(python3 -m) pipenv shell

# server - django makemigrations
(python3 -m) pipenv run makemigrations
# server - django migrate
(python3 -m) pipenv run migrate
# server - django runserver
(python3 -m) pipenv run runserver

```

---

## Setup & Start Server
To run the game, you will need to install all the dependencies (in Pipfile).

Run commands (from this directory):
```
cd lively-lions

python3 --version
> Python 3.8.X

(python3 -m) pip install pipenv
mkdir .venv
(python3 -m) pipenv install

(python3 -m) pipenv run makemigrations
(python3 -m) pipenv run migrate
(python3 -m) pipenv run runserver
```
- open browser (two session)
  - open browser : http://localhost:8000/
  - open browser(with private) :http://localhost:8000/
- Read the tutorial ~~Just Attack Others~~
- Enjoy it

---
## team members
- whywhyy @whywhyy#2263 
- Alex Zorakin @AlexCamachoTacoBellSupreme#1346 
- Gabriel Ruiz @Gabe#7155 
- tienlocnguyen @Pippi#0019 