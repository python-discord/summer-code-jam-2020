# Trivia Tavern by Practical Penguins

## about
This django web application allows people to create and organize trivia events. Participants can then answer trivia question using their phones.

## installation requirement
* python 3.8
* git

## how to use

We are hosting our own app publicly for a limited time at <URL>, but you can easily host this run
this server at home without having to pay for your own server hosting costs.

Scroll down for instructions on this

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

then go to `http://localhost:8000/` in your web browser. You can also access the site using your ngrok url!
