import os
import datetime
from django.shortcuts import render
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
        welcome = f'Thanks for playing, "{fetch_quiz.name}" will begin now!'
        sms_send(welcome, recipient)
        new_quiz = ActiveTriviaQuiz.objects.filter(trivia_quiz=fetch_quiz)
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
        question1 = TriviaQuestion.objects.filter(quiz=fetch_quiz)[0]
        msg = question1.question_text

    else:
        msg = ( 'This number has not started any quizzes. '
                'Please start your quiz by texting START/<quiz#> to start!'
        )

    sms_send(msg, recipient)

    # no page to display, redirect to another
    return HttpResponse(200)
