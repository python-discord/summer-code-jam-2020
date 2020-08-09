# Imaginary Iguanas
# MyPlace

MyPlace is a social media app written in Django, celebrating the MySpace era where personal blogs and social media came together in weird and wonderful harmony.

## Installation

###### Prerequisites:
- Python 3.8
- Pipenv installed in your global environment
- Dependencies from our `imaginary-iguanas/Pipfile`
- Redis server installed on your machine and running on port 6379 (if you're having troubles for Windows you can use [memurai](https://docs.memurai.com/))

1. Clone Git repo (master branch)
2. Activate environment

    For PyCharm: File -> Settings -> Project -> Project Interpreter
    
    Click the gear icon, then select Add. In the popup window, select Pipenv Environment, make sure 'Install packages from Pipfile' is checked, then click OK.

    For terminal: Just cd to imaginary-iguanas, shell into environment `pipenv shell` and install dependencies `pipenv install`

6. Now to initialize the database. 

    You can either cd to `imaginary-iguanas/code_jam` and run `python manage.py makemigrations` and `python manage.py migrate`
    or you can use pipenv scripts `pipenv run make` and `pipenv run migrate`

To run the project, simply open the Terminal in PyCharm, `cd` to `imaginary-iguanas/code_jam` and `python manage.py runserver`
There's a shortcut script for this too `pipenv run start`
You should now be able to access the site through localhost:8000.

## Getting Around

The home page will give you a brief introduction to the features available in MyPlace, but all the links are in the navbar at the top of the page too. You'll need to sign up before you can access any of the other areas of the site, with the exception of All Users.

**Sign Up** - Create a new account

**Log in** - Log in with an existing account

**Profile** - View your profile page as it is currently set up

**Settings** - Personalise your profile/blog by uploading a profile picture, updating your personal details, adding a song, or even writing your own custom CSS. (Hint - We have some example custom CSS templates available for you to try, under the example_templates directory. Just copy and paste one of these into the custom CSS field in your profile settings, save and watch the magic happen!)

**Chat** - Join a chat room to meet other users

**All Users** - See all users currently signed up to the site

**Log Out** - Goodbye!
