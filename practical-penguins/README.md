
# ![Trivia Tavern](trivia_tavern/static/header_logo.png) by Practical :penguin:
 
# Table of Contents

1. [About](#about)
2. [App features](#tour-of-the-app)
3. [Installation](#Installation)
5. [how to run your own server locally](#how-to-run-your-own-server-locally) 
6. [Future Ideas](#Ideas-and-Feature-for-the-future)

## About
This django web application allows people to create and organize trivia events. Participants can then answer trivia
 question using their phones.
 
## App features
We are hosting our app publicly for a limited time at this development [URL](https://a95e3eb77ce9.ngrok.io)

But you can easily host this run this server at home without having to pay for your own server
hosting costs ([see below](#how-to-run-your-own-server-locally)).

For basic operation, you need only create an account, and when you're ready just hit "Run Quiz" to
complete setting up your first quiz session. When you run it, you'll see the current question display

![alt text](screenshots/quiz-run.png?raw=True)

Not sure where to start? We have a few trivia packs pre-made by yours truly!

![alt text](screenshots/trivia_pack_page.PNG?raw=True)

## Installation
This package is tested on python 3.8

git clone and cd to this project with:

```bash
git clone https://github.com/kkawabat/summer-code-jam-2020.git
cd summer-code-jam-2020
cd practical-penguins
```

run setup.py

    python setup.py install
  
**Note: you might run into some difficulty with Pillow on windows machine if so please see [here](#pillow-issues)**

initialize database

```bash
cd trivia_tavern
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/fixture_auth.json
python manage.py loaddata fixtures/fixture_users.json
python manage.py loaddata fixtures/fixture_trivia_packs.json
```

set environment variables to your Twilio account

You can run these commands temporarily from one shell session, but to set them permanently, simply copy the following
into your ~/.bashrc, without the '<>':
```bash
  export TWILIO_ACCOUNT_SID=<your-account-id>
  export TWILIO_AUTH_TOKEN=<your-account-secret>
  export TWILIO_NUMBER=<your-number>
```

Environment variables in Windows can be set similarly by adding them to System>Advanced>Environment Variables

####Pillow issues
NOTE: We have encountered installation issues when trying to install Pillow on windows
(see [here](https://stackoverflow.com/questions/41188838/cant-install-pillow-in-windows)).
Try to install Pillow before the above command if there are issues relating to `Pillow`.

## how to run your own server locally

So you wanna be your own sysadmin? Fortunately, you can do this at *almost* no cost to yourself!

In order to do this, you'll need 1) a Twilio account to receive and send text messages, 2) an ngrok
account in order to create a public webhook to "listen" for incoming texts.

Sound complicated? Don't worry! We have pictures to help.

First set up a new Twilio account at https://twilio.com/ and start your free trial.

Note, however, there are two important drawbacks to trial accounts
1) Trial accounts can ONLY send texts to numbers registered in advance
2) Any text sent from a trial account will come prepended with 'This came from a Twilio Trial Account - '

For those reasons, we highly recommend biting the bullet and paying the minimum $20 so you can send your trivia at will! That should be enough for about 2,000 texts, probably more.

Next setup an account on https://ngrok.com/ and under the 'Setup & Installation' download the ngrok tool for your OS. Here's how the setup looks like on Linux for example

![alt text](screenshots/ngrok-linux-setup.png?raw=True)

By default, Django servers run on port 8000 so run this on a command line:
```bash
ngrok http 8000
```

You should now see a random looking url on your command window

![alt text](screenshots/ngrok-running.png?raw=True)

This is where you will receive texts to. So now we need to set up Twilio to listen on that URL.

Go back to your Twilio account, on the top left, you should see a little bubble under the Home button. Click that and navigate to 'Phone Numbers' to see your currently active phone numbers and click the number you want to use. You should now be on the configuration page for your number. Here's what ours looks like

![alt text](screenshots/twilio-setup1.png?raw=True)

Scroll down a bit to the 'Messaging' section. Copy and paste your ngrok url into the 'A message comes in' field. Then add '/sms/' to the end of it. DO NOT forget the trailing slash!

![alt text](screenshots/twilio-setup2.png?raw=True)

Now you can finally run your server!

run the below command

    python manage.py runserver

then go to ` http://127.0.0.1:8000/` in your web browser to view locally. You can also access the site using your ngrok url!

If you want a more permanent solution, you can host this on web hosting service like AWS. In that case, you would use your static IP instead of the ngrok URL.

Note in order to have the full functionality of Trivia Tavern you will need to setup your own twilio account/number.
The app will need the following 3 environment variables set at run time:
- TWILIO_NUMBER
- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN  

see [Twilio documentation](https://www.twilio.com/docs) for more details.

## Future Ideas
- implement different question types rather than free form Q&A
    - questions with multiple choice answers
    - question with embedded pictures
    - questions with multiple right answers
- flesh out the designs of the webpage, some exmaples:
    - ~~the home page should look like a bulletin board~~ done!
    - ~~Buttons should look like stamps~~ done!
    - the "Run Trivia" page can look like a bookshelf
    - the "Create Trivia Pack" form can look like an open book  
- Add Timer functionality - During a quiz the quiz master can add additional time to a question or pause the timer
- Dynamically see who has answered the question/signed up for the quiz - requires javascript knowledge that requires
time to learn
- Allow session master to automatically invite their friends by adding their number manually during session setup
- save stats of players to their profile (e.g. how many wins, what they recently participated in, etc.)
- expand this app to not only do quizzes but other text based games, some ideas:
    - choose your own adventure through text message
