<div align="center">
  
![socl -crop](https://user-images.githubusercontent.com/20405311/89612675-021b5700-d89e-11ea-8c0e-f6825f1672fd.jpg)
# SoCL Media 
**SoCommandLine Media**<br>
By a bunch of Annoyed Alligators
  
---

<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25.gif" border="0" alt="Made with Django." title="Made with Django." /></a>  ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi)

---

</div>

## Index
- [About](#about)
- [Setup](#setup)
- [Usage](#usage)
  - [Commands](#commands)
- [File Structure](#file-structure)


## About
Command Line Interfaces are one of the oldest Human-Computer interaction methods. So much so that they were thought of as the *only* way of interacting with a computer even much later than the IBM computers of the early 80s. Right around the same time, some dudes at Apple were coming up with the first basic GUI. The early version of internet had long been existing since ARPANET grew from 1970s. <br>
So, what if some crazy ~~lonely~~ dude had this idea of making what we now call "Social Media" back then?
Surely it would have been a weird amalgamtion of a CLI controlled GUI, even the web pages! So here's a **SoCL Media**.


-------------------- SCREENSHOT HERE

## Setup
1. Clone this repository by running `git clone https://github.com/akshgpt7/summer-code-jam-2020`.
2. Make sure you have `pipenv` installed in your system. If not, do it by `pip install pipenv`.
3. cd to the team's folder by `cd summer-code-jam-2020/annoyed-alligators`.
4. To activate a virtual environment for the project, run `pipenv shell`. After this, you'll be inside the virtual environment.
5. Install the dependencies by running `pipenv install`.
(migrations)
(populate db)
6. Run the Dev Server by `python3 manage.py runserver`.

## Usage
Just like you use any other social media platform, but there's a catch. You have a command for almost everything!<br>
Create an account and log in through it to connect with your friends and access various features of SoCL Media.<br>
*(Pro tip: Imagine yourself to be in the 80s for the best feels!)*

#### Commands:
(Type `[command name] --help` for details and usage of a particular command)
- `help`: Display a list of all available commands
- `home`: Jump to home screen (feed)
- `view-post`: View a particular post by its number
- `logout`: Log Out of your account
- `signup`: Register a new user
- `change-password`: Change your password
- `message`: Send a personal message to any user
- `message-box`: View your received messages
- `profile`: View any user's profile 
- `news`: Get the latest news articles and read them

## File Structure
```
.
├── db.sqlite3
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── socl_media
    ├── apps
    │   ├── chat
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── __init__.py
    │   │   ├── migrations/
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── feed
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── forms.py
    │   │   ├── __init__.py
    │   │   ├── migrations/
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── README.md
    │   ├── terminal
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── command_runner.py
    │   │   ├── commands.py
    │   │   ├── __init__.py
    │   │   ├── migrations/
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   └── users
    │       ├── admin.py
    │       ├── apps.py
    │       ├── forms.py
    │       ├── __init__.py
    │       ├── migrations/
    │       ├── models.py
    │       ├── signals.py
    │       ├── tests.py
    │       ├── urls.py
    │       └── views.py
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── static
    │   ├── favicon.ico
    │   └── media
    │       ├── default.png
    │       ├── post_images/
    │       ├── profile_pics/
    │       └── README.md
    ├── templates
    │   ├── base.html
    │   ├── chat
    │   │   └── message-box.html
    │   ├── feed
    │   │   ├── post_confirm_delete.html
    │   │   ├── post_detail.html
    │   │   ├── post_form.html
    │   │   └── post_list.html
    │   ├── README.md
    │   ├── terminal.html
    │   └── users
    │       ├── login.html
    │       ├── password_change_done.html
    │       ├── password_change_form.html
    │       ├── password_reset_complete.html
    │       ├── password_reset_confirm.html
    │       ├── password_reset_done.html
    │       ├── password_reset.html
    │       ├── profile_edit.html
    │       ├── profile.html
    │       └── signup.html
    ├── urls.py
    └── wsgi.py
```
