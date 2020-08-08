# Trivia Tavern by Practical Penguins

## about
This django web application allows people to create and organize trivia events. Participants can then answer trivia
 question using their phones.

## installation requirement
* python 3.8
* git

## installation
git clone and cd to this project with:

```bash
git clone https://github.com/kkawabat/summer-code-jam-2020.git
cd summer-code-jam-2020
cd practical-penguins
```

run setup.py

    python setup.py install

NOTE: We have encountered installation issues when trying to install Pillow on windows 
(see [here](https://stackoverflow.com/questions/41188838/cant-install-pillow-in-windows)).
Try to install Pillow before the above command if there are issues relating to `Pillow`.

initialize database

```bash
cd trivia_tavern
python manage.py migrate
python manage.py makemigrations
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

## start server locally
run the below command

    python manage.py runserver

then go to ` http://127.0.0.1:8000/` in your web browser. 

Note in order to have the full functionality of Trivia Tavern you will need to setup your own twilio account/number.
The app will need the following 3 environment variables set at run time:
- TWILIO_NUMBER
- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN  

see [Twilio documentation](https://www.twilio.com/docs) for more details.

## Ideas and Feature for the future 
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
- Allow sessino master to automatically invite their friends by adding their number manually during session setup
- save stats of players to their profile (e.g. how many wins, what they recently participated in, etc.) 
- expand this app to not only do quizzes but other text based games, some ideas:
    - choose your own adventure through text message



