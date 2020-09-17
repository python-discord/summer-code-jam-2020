
# PySpace!

## Info
Our project is a social media platform, based off of the popular MySpace website, hence the name of our project; PySpace. On our platform users can create posts, like each others posts, make comments on each others posts, and follow each other, just as they could on our inspiration site, myspace. 

## Setup:
In order to setup this project you'd need to have nodejs installed (and python of course).
Node.js Installation Link: https://nodejs.org/en/download/.

first we'll start with running the backend (or in other words, the API):
1. Open your preffered console/terminal.
2. cd into the PySpace directory - Example if you've installed the summer code jam fork on your Desktop:
```
cd path/to/desktop/summer-code-jam-2020/graceful-grasshoppers/PySpace
```
3. Create a virtual environment.
- MacOS or Linux (bash): 
```
python3 -m venv pyspace
source pyspace/bin/activate
```
- Windows (cmd): 
```
py -m venv pyspace
.\pyspace\Scripts\activate
```
Now you have your virtual environment activated. (to be sure, make sure the prompt is now `(pyspace) the/path/of/the/current/folder`)
4. Install the requirements.
```
pip install -r requirements.txt
```
5. Make Migrations.
- MacOS or Linux (bash): 
```
python3 makemigrations
python3 makemigrations posts
python3 migrate
```
- Windows (cmd): 
```
py makemigrations
py makemigrations posts
py migrate
```

6. Run server:
- MacOS or Linux (bash): 
```
python3 ./manage.py runserver
```
- Windows (cmd): 
```
py .\manage.py runserver
```

### Now we're done from running the backend! keep the console open and let's headover to running the frontend now.
1. Again, open your preffered console/terminal.
2. cd into the pyspace-frontend directory - Example if you've installed the summer code jam fork on your Desktop:
```
cd path/to/desktop/summer-code-jam-2020/graceful-grasshoppers/pyspace-frontend
```
3. Install the dependencies:
```
npm install
```
4. Build and run:
```
npm run build
npm run serve
```

You should be done now!! headover to http://localhost:8080/ and enjoy!

## What does it look like?
#### Welcome page
![home](https://imgur.com/9FzKzxY.jpg)
#### Profile page 
We have kept the original design of the profile page simple and retro style as you can see here:
![homepage](https://imgur.com/Nc0JuI7.jpg)
It displays about the user along with there posts/friends and comments about the user! Just like the good old days.
#### Friends page
You can also view a users friends, as can be seen here:
![Friends](https://imgur.com/9qJQYMy.jpg)
#### Random
This page lets you see a random user!
![Randy](https://imgur.com/sXfjCKt.jpg)
#### View post
This lets you view a post to the site
![post](https://imgur.com/Ad3bDWg.jpg)
#### Create post
If the user wants to create a new post then they will be greeted with this:
![newpost](https://imgur.com/xq0ubBV.jpg)

## How have we created this?

We have used vue for the frontend and django for the backend.

## Creators:

nashetime#2951 (TEAM LEADER / FRONTEND DEV)
[GITHUB](https://github.com/georgemunyoro)

xo#1111 (BACKEND DEV)
[GITHUB](https://github.com/cswil)

c3a#1737 (BACKEND/FRONTEND DEV)
[GITHUB](https://github.com/Chris-C3A)

DAzVise#1666 (BACKEND)
[GITHUB](https://github.com/DAzVise)

Vthechamp#3454 (BACKEND/FRONTEND DEV)
[GITHUB](https://github.com/Vthechamp22)
