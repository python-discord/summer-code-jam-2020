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
First, clone the repository and cd to the directory. We'll cd into the `Backend` folder to setup the server, first. 
```
git clone https://github.com/JetDeveloping/summer-code-jam-2020.git
cd summer-code-jam-2020/wiggly-weasels/Backend
```
Then, we need to install the required packages:
```
pip install requirements.txt
```
Now, all we need to do is run the server code!
