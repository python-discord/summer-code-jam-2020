import os
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

from trivia_builder.models import TriviaQuiz, TriviaQuestion
from trivia_runner.models import ActiveTriviaQuiz, Player
# Create your views here.


def sms_send(msg, recipient):
    """sms_send will send a message 'msg' to a 'recipient'
    This is not really a view method, but a help method for other classes
    and views (for example the user views)
    """
    twilio_account_sid = settings.HOST_TWILIO_SID
    twilio_auth_token = settings.HOST_TWILIO_AUTH_TOKEN
    twilio_number = settings.HOST_TWILIO_NUMBER
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body=msg,
        from_=twilio_number,
        to=recipient
    )


def register(phone_number):
    return Player.objects.create(
        name='name',
        number=phone_number,
    )


def start_quiz(fetch_quiz, player):
    question1 = TriviaQuestion.objects.filter(quiz=fetch_quiz)[0]
    msg = question1.question_text
    sms_send(msg, player.phone_number)


@csrf_exempt
def sms_reply(request):
    """sms_reply is a handler method that triggers when the url 'sms' is
    navigated to. Your Twilio account should be configured to point to:
    <this-site>/sms so that those texts will be recieved here and processed
    by this function
    """
    # Get details about the message that just came in
    recipient = request.POST.get('From', None)
    body = request.POST.get('Body', None)

    # Get info on current quizzes
    available_quizzes = TriviaQuiz.objects.all()

    # Check if the message is a request to start a quiz, or a response to a
    # question, otherwise, send back an error message
    if body.split('/')[0].upper() == 'START':
        qid = int(body.split('/')[1])
        fetch_quiz = TriviaQuiz.objects.filter(pk=qid)[0]
        welcome = f'Thanks for playing, "{fetch_quiz.name}" will begin soon!'
        sms_send(welcome, recipient)
        new_player = register(recipient)
        start_quiz(fetch_quiz, new_player)
        # This logic should be moved to the quizmaster side actually
        #new_quiz = ActiveTriviaQuiz.objects.filter(trivia_quiz=fetch_quiz)
        #if new_quiz.exists():
        #    new_quiz.players.append(recipient)
        #else:
        #    new_quiz = ActiveTriviaQuiz.create(
        #        trivia_quiz = fetch_quiz,
        #        session_code = qid,
        #        current_question_index = 1,
        #        session_master = fetch_quiz.author,
        #        start_time = datetime.datetime.now(),
        #        players = [recipient] # not sure what to do here yet
        #    )
                                                #testing only, real value
                                                #should be from the newly
                                                # made active quiz

    elif Player.objects.filter(phone_number=recipient).exists():
        # if quiz started, interpret as answer
        # else tell the player the quiz hasn't started yet
        pass
    else:
        msg = ( 'This number has not started any quizzes. '
                'Please start your quiz by texting START/<quiz#> to start!'
        )

    sms_send(msg, recipient)

    # no page to display, redirect to another
    return redirect('home')
