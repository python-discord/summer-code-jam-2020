<img src='./horsecodejamlogo.png'; alt='Logo'; align='center'>

<hr>

### Installation:
1. Clone repository

2. Create virtual environment for this project ([virtualenv](https://pypi.org/project/virtualenv/))

3. Activate your virtual environment 

4. Navigate to /histerical-horses directory and `pip install -r requirements.txt`
 *this will install every required module for the project* 
 
5. Create environment variable for Django secret key: search "environment variable" in windows search bar => 
edit the system environment variables => environment variables => user variables for "current user's name here" => new =>
variable name == summer_jam_secret_key, variable value == (use secret key that should be pinned in hysterical-horses chat)

6. run `python manage.py migrate` in order for the site to behave properly (the database
file will be ignored when committing to avoid merge conflicts)
