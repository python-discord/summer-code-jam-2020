from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from trivia_builder.models import TriviaQuestion
from trivia_runner.models import ActiveTriviaQuiz, Player, Answer
from .models import ScoreTracker


class SMSBot:
    """SMSBot is a helper class to implement the main receving 'sms_reply'
    functions and process the input received from texts
    @send: send a string 'msg' to a phone number 'recipient'
    @register: register a new player with a 'phone_number' for requested 'active_quiz'
    @send_question: sends question #'qnumber' from a 'trivia_quiz' to 'player'
    """

    @staticmethod
    def send(msg: str, recipient):
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
        return message

    @staticmethod
    def register(phone_number, active_quiz):
        """registers a default player account with the ActiveTriviaQuiz 'quiz'
        and a 'phone_number'
        """

        player = Player.objects.create(team_name='', active_quiz=active_quiz, phone_number=phone_number,)
        return player

    @staticmethod
    def send_question(question, player):
        """sends the specified question 'question' to 'player'
        """
        msg = f'Question#{question.question_index}: {question.question_text}'
        SMSBot.send(msg, player.phone_number)

    @staticmethod
    def register_with_code(number, active_quiz):
        welcome = (f'You registered to play "{active_quiz.trivia_quiz.name}." '
                   f'Please choose a team name to join'
                   f'If you didn\'t mean to do this, text !quit at any time')
        SMSBot.send(welcome, number)
        new_player = SMSBot.register(number, active_quiz)
        new_player.save()
        active_quiz.players.add(new_player)
        active_quiz.save()

    @staticmethod
    def pick_team(team, player):
        player_quiz = player.active_quiz
        player.team_name = team
        player.save()
        msg = (f'Thanks for playing! Your team is "{player.team_name}"'
               f'"{player_quiz.trivia_quiz.name}" will begin soon!')
        ScoreTracker.objects.create(player_phone=player.phone_number,
                                    team_name=player.team_name,
                                    session_code=player_quiz.session_code)
        SMSBot.send(msg, player.phone_number)

    @staticmethod
    def player_quit(player):
        player_quiz = player.active_quiz
        from_ = player.phone_number
        score_track = ScoreTracker.objects.get(player_phone=player.phone_number,
                                               session_code=player_quiz.session_code)
        player.delete()
        score_track.delete()
        SMSBot.send('You have left the quiz.', from_)

    @staticmethod
    def pre_quiz(body, player):
        player_quiz = player.active_quiz
        if body.split('/')[0].upper() == '!EDIT':
            player.team_name = body.split('/')[1]
            player.save()
            score_track = ScoreTracker.objects.get(player_phone=player.phone_number,
                                                   session_code=player_quiz.session_code)
            score_track.team_name = player.team_name
            score_track.save()
            SMSBot.send(f'Your team has been updated! You are now on team "{player.team_name}"', player.phone_number)
        else:
            please_wait = ('The host hasn\'t started the quiz yet, patience is a virtue! '
                           'If you want to change teams, text !EDIT/newteamname before the quiz starts. '
                           'Please make sure you let your teammates know though!'
                           )
            SMSBot.send(please_wait, player.phone_number)

    @staticmethod
    def evaluate_answer(body, player):
        player_quiz = player.active_quiz
        current_question = TriviaQuestion.objects.get(quiz=player_quiz.trivia_quiz,
                                                      question_index=player_quiz.current_question_index)

        score_track = ScoreTracker.objects.get(player_phone=player.phone_number,
                                               session_code=player_quiz.session_code)
        if score_track.answered_this_round:
            return SMSBot.send('You already answered! Don\'t cheat!', player.phone_number)

        ans = Answer.objects.create(value=body, player=player, question=current_question)
        if ans.is_correct():
            score_track.points += 1
        score_track.answered_this_round = True
        score_track.save()
        msg = 'Thanks for your answer! Please wait for the next question...'
        return SMSBot.send(msg, player.phone_number)

    @staticmethod
    def player_timeout(active_trivia_quiz):
        for player in Player.objects.all():
            score_track = ScoreTracker.objects.get(player_phone=player.phone_number,
                                                   session_code=active_trivia_quiz.session_code)

            if not score_track.answered_this_round:
                current_question = TriviaQuestion.objects.get(quiz=active_trivia_quiz.trivia_quiz,
                                                              question_index=active_trivia_quiz.current_question_index)
                Answer.objects.create(value="", player=player, question=current_question)
                score_track.answered_this_round = True
                score_track.save()
            SMSBot.send('TIME IS UP. NO MORE ANSWERS!', player.phone_number)

    @staticmethod
    def send_all_questions(active_trivia_quiz):
        cur_question = TriviaQuestion.objects.get(quiz=active_trivia_quiz.trivia_quiz,
                                                  question_index=active_trivia_quiz.current_question_index)
        for player in Player.objects.all():
            score_track = ScoreTracker.objects.get(player_phone=player.phone_number,
                                                   session_code=active_trivia_quiz.session_code)
            score_track.answered_this_round = False
            score_track.save()
            SMSBot.send_question(cur_question, player)

    @staticmethod
    def calculate_results(active_trivia_quiz):
        # must be filter in order to get multiple questions
        question_set = TriviaQuestion.objects.filter(quiz=active_trivia_quiz.trivia_quiz)

        score_list = ScoreTracker.get_team_score_list(active_trivia_quiz.session_code)
        winner = ScoreTracker.winner(score_list)
        if winner is None:
            winner = "No one participated :("

        tally_results = {'winner': winner,
                         'score_list': score_list}
        # release players here
        for player in Player.objects.all():
            score_track = ScoreTracker.objects.get(player_phone=player.phone_number,
                                                   session_code=active_trivia_quiz.session_code)

            goodbye = (f'The session has ended, thanks for playing!\n'
                       f'Team {winner} was the winner!\n'
                       f'Your score was: {score_track.points}/{len(question_set)}'
                       )

            SMSBot.send(goodbye, player.phone_number)
            SMSBot.send(player.get_answers(), player.phone_number)
            player.delete()
        return tally_results

    @staticmethod
    def send_quiz_invite(number, active_trivia_quiz):
        intro = (f'Hello! You\'ve been invited to play {active_trivia_quiz.trivia_quiz.name}'
                 f'If you\'re not game, just text back !quit we won\'t bother you!'
                 f'Otherwise, please text back a team name to join')
        SMSBot.send(intro, number)
        SMSBot.register(number, active_trivia_quiz)


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
    session_codes = [q.session_code for q in available_quizzes]

    if body.upper() == '!QUIT':
        SMSBot.player_quit(player)
        return redirect('/')

    if player.exists():
        player = player.first()
        player_quiz = player.active_quiz
        if player.team_name == '':
            team_names = [t.team_name for t in Player.objects.all()]
            if body in team_names:
                SMSBot.send('Sorry that name is taken!', from_)
            else:
                SMSBot.pick_team(body, player)

        elif player_quiz.current_question_index == 0:
            SMSBot.pre_quiz(body, player)

        else:
            # Player is answering the question
            SMSBot.evaluate_answer(body, player)
            # Optional, send players their score after every question
            # SMSBot.send(f'Your current score is: {player.points}/{len(question_set)}', from_)

    elif body in session_codes:
        fetch_quiz = available_quizzes.get(session_code=body)
        SMSBot.register_with_code(from_, fetch_quiz)

    else:
        msg = ('This number has not started any quizzes. '
               'Please send a valid session code to start!'
               )
        SMSBot.send(msg, from_)

    # no page to display, sorry :(, redirect to another
    return redirect('/')
