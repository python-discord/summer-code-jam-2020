
# PySpace!

## Info
Our project is a social media platform, based off of the popular MySpace website, hence the name of our project; PySpace. On our platform users can create posts, like each others posts, make comments on each others posts, and follow each other, just as they could on our inspiration site, myspace. 

## Setup:
Uh, so, anyways, to run this project, you would need to have node installed, too bad if you don't. Head over to nodejs.org and grab yours. got it? Good.<br>

Now go to a terminal and `cd` into this project. Now, `cd` into `pyspace-frontend` and run `npm install`. It should have worked. Probably. If it doesn't, and gives a `404`, the `npm` server is probably down in your region, so you have two options now:
1. Use a VPN and try to run it
2. Move onto another project and come back to this later.

So now that you ran that, ~~one more~~ a couple more commands are left: run `npm run serve` in this terminal. Let it be, and open up another terminal. Again, navigate to this project, and then `cd` into `Pyspace`. Now, this step is optional, but necessary. Wiat what. Nvm, just create a virtual environment by running `python3 -m venv venv`. After that has completed:
* If you are on bash, run `source venv/bin/activate`
* If you are on windows `cmd`, simply do `.\venv\Scripts\activate`
* Or if you are on windows `powershell`, do `.\venv\Scripts\Activate.ps1`

Good, now you have your virtual environment activated. (to be sure, make sure the prompt is now `(venv) the/path/of/the/current/folder`)

So now run `python3 -m pip install -r requirements.txt` to install the necessary packages. Once that is finished, run `python3 manage.py runserver`


Now go to your browser and head over to localhost:8080, and voila! Exploreeeee!

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
