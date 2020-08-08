from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from trivia_builder.models import TriviaQuiz, TriviaQuestion
from trivia_runner.models import ActiveTriviaQuiz, Player
from .models import ScoreTracker

class SMSBot():
    """SMSBot is a helper class to implement the main receving 'sms_reply'
    functions and process the input received from texts
    @send: send a string 'msg' to a phone number 'recipient'
    @register: register a new player with a 'phone_number' for requested 'active_quiz'
    @send_question: sends question #'qnumber' from a 'trivia_quiz' to 'player'
    """
    def send(msg, recipient):
        """send will send a message 'msg' to a 'recipient'
        This is not really a view method, but a helper method for the main
        sms_reply method
        """
        twilio_number = settings.HOST_TWILIO_NUMBER
        client = settings.TWILIO_CLIENT
        message = client.messages.create(
            body=msg,
            from_=twilio_number,
            to=recipient
        )

    def delayed_send(msg, recipient, delay):
        #This function does not work yet
        #time.sleep(delay)
        SMSBot.send(msg, recipient)

    def register(phone_number, active_quiz):
        """registers a default player account with the ActiveTriviaQuiz 'quiz'
        and a 'phone_number'
        """
        return Player.objects.create(
            name='',
            active_quiz=active_quiz,
            phone_number=phone_number,
        )

    def send_question(question, player):
        """sends the specified question 'question' to 'player'
        """
        msg = question.question_text
        SMSBot.send(msg, player.phone_number)

@csrf_exempt
def sms_reply(request):
    """sms_reply is a handler method that triggers when the url 'sms' is
    navigated to. Your Twilio account should be configured to point to:
    <this-site>/sms so that those texts will be recieved here and processed
    by this function. You can think of this like a 'main' method

    For testing purposes, the developer recommends ngrok to host a temporary
    server and domain name that points to your localhost
    (for example http://a2b0fd3c60b6.ngrok.io) and set your
    twilio account settings in Phone Numbers > Manage Numbers > Active numbers
    under "Messaging" and set a webhook to <url>/sms/ BUT do not forget the
    trailing slash!
    """
    # Get details about the message that just came in
    from_ = request.POST.get('From', None)
    body = request.POST.get('Body', None)

    # check if the text is from a registered Player, can be null
    player = Player.objects.filter(phone_number=from_)
    available_quizzes = ActiveTriviaQuiz.objects.all()
    session_codes = [ q.session_code for q in available_quizzes ]

    if player.exists():
        player = player.first()
        player_quiz = player.active_quiz
        if player.name == '':
            # Player picks a username
            player.name = body
            player.save()
            msg = ( f'Thanks for playing, {player.name}! '
                f'"{player_quiz.trivia_quiz.name}" will begin soon!'
            )
            ScoreTracker.objects.create(player_name=player.name,
                                        session_code=player_quiz.session_code)
            SMSBot.send(msg, from_)

        elif player_quiz.current_question_index == 0:
            SMSBot.send('The host hasn\'t started the quiz yet, patience is a virtue!', from_)

        else:
            # Player is answering the question
            current_question = TriviaQuestion.objects.get(quiz=player_quiz.trivia_quiz,
                                                      question_index=player_quiz.current_question_index)
            correct_answer = current_question.question_answer
            score_track = ScoreTracker.objects.get(player_name=player.name, session_code=player_quiz.session_code)
            if score_track.answered_this_round == True:
                msg = 'You already answered! Don\'t cheat!'
            elif body.upper() == correct_answer.upper():
                msg = 'That\'s correct!'
                score_track.points += 1
            else:
                msg = f'Wrong, the right answer was "{correct_answer}"'
            score_track.answered_this_round = True
            score_track.save()
            SMSBot.send(msg, from_)
            SMSBot.send(f'Your current score is: {player.points}/{len(question_set)}', from_)

    elif body in session_codes:
        fetch_quiz = available_quizzes.get(session_code=body)
        welcome = ( f'You registered to play "{fetch_quiz.trivia_quiz.name}." '
                    f'Please choose a player name'
        )
        SMSBot.send(welcome, from_)
        new_player = SMSBot.register(from_, fetch_quiz)
        new_player.save()
        fetch_quiz.players.add(new_player)
        fetch_quiz.save()

    else:
        msg = ( 'This number has not started any quizzes. '
                'Please send a valid session code to start!'
        )
        SMSBot.send(msg, from_)

    # no page to display, sorry :(, redirect to another
    return redirect('/')