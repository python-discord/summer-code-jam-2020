
# Graceful Grasshoppers
### Intro:
So... welcome! This is our project, Pyspace, and if you didn't already realise, Myspace. Even tho idk what that is. Probably an old facebook. 

### Setup:
Uh, so, anyways, to run this project, you would need to have node installed, too bad if you don't. Head over to nodejs.org and grab yours. got it? Good.<br>

Now go to a terminal and `cd` into this project. Now, `cd` into `pyspace-frontend` and run `npm install`. It should have worked. Probably. If it doesn't, and gives a `404`, the `npm` server is probably down in your region, so you have two options now:
1. Use a VPN and try to run it
2. Move onto another project and come back to this later.

So now that you ran that, ~~one more~~ a couple more commands are left: run `npm run serve` in this terminal. Let it be, and open up another terminal. Again, navigate to this project, and then `cd` into `Pyspace`. Now, this step is optional, but necessary. Wiat what. Nvm, just create a virtual environment by running `python3 -m venv venv`. After that has completed:
* If you are on bash, run `source venv/bin/activate`
* If you are on windows `cmd`, simply do `.\venv\Scripts\activate`
* Or if you are on windows `powershell`, do `.\venv\Scripts\Activate.ps1`

Good, now you have your virtual environment activated. (to be sure, make sure the prompt is now `(venv) the/path/of/the/current/folder`)

So now run `python3 -m pip install -r requirements.txt` to install the necessary packages. Once that is finished, run `python3 manage.py makemigrations`, `python3 manage.py migrate` and `python3 manage.py runserver`. Sorry.

Now go to your browser and head over to localhost:8080, and voila! Exploreeeee!