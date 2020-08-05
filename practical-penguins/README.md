# Trivia Tavern by Practical Penguins

## about
This django web application allows people to create and organize trivia events. Participants can then answer trivia question using their phones.

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

NOTE: We have encountered installation issues when trying to install Pillow on windows (see [here](https://stackoverflow.com/questions/41188838/cant-install-pillow-in-windows)).
Try to install Pillow before the above command if there are issues relating to `Pillow`.

initialize database

```bash
cd trivia_tavern
python manage.py migrate
python manage.py makemigrations
```

set environment variables to your Twilio account

You can run these commands temporarily from one shell session, but to set them permanently, simply copy the following into your ~/.bashrc, without the '<>':
```bash
  export TWILIO_ACCOUNT_SID=<your-account-id>
  export TWILIO_AUTH_TOKEN=<your-account-secret>
  export TWILIO_NUMBER=<your-number>
```

Environment variables in Windows can be set similarly by adding them to System>Advanced>Environment Variables

## start server locally
run the below command

    python manage.py runserver

then go to ` http://127.0.0.1:8000/` in your web browser
