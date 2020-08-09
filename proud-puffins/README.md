![Proud Puffins](djangoProject/static/images/Proud_Puffin_banner.png)
# Proud Puffins

Our take on the topic of early internet was to make a dating website, that was so 90's you probably threw up a little in your mouth. So ninties that you partied like it was 1999. We tried to add as much early internet obnoxiousnesses to it, to really make you love the 2020's, even with Covid around. Features such as in browser music, colored scroll bars, marquee text and of course Fabio. Unfortunately we won't get credit for any of it, because it was all hard coded in HTML. However, the part of the site that is Djangos back end is a system for matching you to the love of your life, albeit a fake love interest. Like, Dislike your way into the hearts of those you might never get to see in real life. We hope you enjoy.

We be Puffins, and we be proud!
* ergomacros
* ImaMoonky
* PDXCardinal78
* XPOjabar
* rr

## Requirements
- Python3.8+
- Django>=3
- Pillow>=7
- pathlib>=1
- django-random-image-from-folder>=0.0.3
- django-crispy-forms>=1.9.2

## Loading the App
- Download or pull a clone of this directory.
- Create a virtual environment using the tools you like best.
- In the terminal cd into the directory djangoProjects. This should be the location of the manage.py file.
- Run ```python3 puffin_setup.py```
- This should make all your migrations, pre load the database with data and start your server.
- Open your favorite browser to 127.0.0.1 to launch app.
- IF you have issues running this, then follow the instructions outlined in the Alternative method below.

## Alternative Method
- Download or pull a clone of this directory.
- Create a virtual environment using the tools you like best.
- Go to proud-puffins directory and install the required packages using ```pip3 install -r requirements.txt```
- In the terminal cd into the directory djangoProjects. This should be the location of the manage.py file.
- Run ```python3 manage.py makemigrations```
- Run ```python3 manage.py migrate```
- Run ```python3 manage.py loaddata users.json```
- Run ```python3 manage.py loaddata profiles.json``` (First users.json then profiles.json)
- Run server using ```python3 manage.py runserver```

## How to use
- Once the App is loaded, visit ```http://127.0.0.1:8000/```
- Register/Login by pressing on the door or click on the login button in the NavBar.
- If you have just registered and logged in, you will be asked to fill in the profile details.
- Now you can start matching by clicking on 'Match Me' in your profile page.
- Once in, you can like or unlike profiles. To move on to the next one, press 'Next profile' button.
- If the other person likes you too, they will appear on your 'mymatches' page (link present in your profiles page) and their email will be shared with you.
- You can see the profiles you've liked in the 'My Likes' page (link present in your profiles page).

### Note:
You may receive lint errors saying ```earlydating.signals was imported but not used in app.py```. Despite those errors we needed it be like that for the working of post_save signals.

## [MIT license](../LICENSE)

## [Credits and sources](Credits%20and%20sources.md)

