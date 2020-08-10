# Flashback
Flashback is an awesome, retro IRC based app built using Django (and the Django Rest Framework) for our backend as well as React for our frontend!

## How to use
Once you login or sign up to Flashback, you have access to the terminal! Here you run a few commands. You can connect to group chats, which allow you to contact chat with other Flashback users. You can also create your own group. We can use the `create` command to create a new group, and the `join` command to join it. Let's try it:
```
>create DoggoFanClub
Creating Group DoggoFanClub

>join DoggoFanClub
Joining Group DoggoFanClub
```

Join can also be used to access groups that have been developed by other members of the community. Once you are in a group, you can use `send` to send messages, `read` to read the newest messages, and `exit` to exit the group. However, whenever you send a message, Flashback will display the messages that came before the message that you had just sent. Here is an example of interactions within groups!
```
>join SomeGroup
Joining SomeGroup

Alice: Hello, is anyone there?
>send Hey Alice!
Bob: Hey Alice!

>read
Alice: Hey Bob
```

## Installation Instructions
Installation is simple. I will assume that you have `npm` and Python already installed!:

### Server Setup
First, clone the repository and cd to the directory. We'll cd into the `Backend` folder to setup the server, first. 
```
git clone https://github.com/JetDeveloping/summer-code-jam-2020.git
cd summer-code-jam-2020/wiggly-weasels
```
First, create a virtual environment and activate it. Then, we need to install the required packages:
```
pip install -r requirements.txt
```
Finally, we need to install postgressql and create a Database called fbdb.
```
#Mac
brew doctor
brew update
brew install libpq
brew link --force libpq ail

#Linux
sudo apt-get update
sudo apt install postgresql postgresql-contrib

#Windows
Download it from here: https://www.postgresql.org/download/windows/

```

You can start Postgres by running `psql`(Linux:`sudo -u postgres psql`). Then you can run `CREATE DATABASE fbdb;`. Make sure the DB server is set to localhost and the port is set to `5443`
You want to make sure that you have a user named `postgres` with the password as `postgres` as well. 
Now, all we need to do is migrate and run the server code! 
```
#Change to the Backend/flashback directory
cd Backend/flashback

#Then make migrations
python3 manage.py makemigrations
python3 manage.py migrate

#Start the server (Warning: Make sure this server is running before site setup)
python3 manage.py runserver


```
<!-- Make sure you are in `wiggly-weasels/Backend/flashback`. Then run the server by running: `python3 manage.py runserver`.  -->

### Site Setup
While the Django server is running. Start a new terminal instance. We will start by assuming that you are in the `summer-code-jam-2020/wiggly-weasels` folder. We can run the following commands to get into the React project folder so we can install our project packages! 
```
cd Frontend/flashback
npm install && npm start
```
Installing the packages is simple! Just type `npm install`! Finally, to run our site, type `npm start`.

### Screenshots
![IRC Client](https://raw.githubusercontent.com/JetDeveloping/summer-code-jam-2020/master/wiggly-weasels/screenshots/IRC1.png)

![IRC Login](https://raw.githubusercontent.com/JetDeveloping/summer-code-jam-2020/master/wiggly-weasels/screenshots/IRC2.png)

