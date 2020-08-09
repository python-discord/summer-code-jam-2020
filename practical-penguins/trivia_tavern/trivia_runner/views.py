from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import DeleteView, ListView

from trivia_builder.models import TriviaQuestion
from trivia_runner.models import ActiveTriviaQuiz, Player
from twilio_messenger.views import SMSBot
from twilio_messenger.views import ScoreTracker
from django.views.decorators.csrf import csrf_exempt


class ActiveTriviaQuizListView(ListView):
    model = ActiveTriviaQuiz
    template_name = 'active_sessions.html'
    context_object_name = 'active_quizzes'
    ordering = ['-start_time']
    paginate_by = 10


def setup(request, active_trivia_quiz):
    return render(request, 'activequiz_setup.html', {'active_trivia_quiz': active_trivia_quiz})


def times_up(request, active_trivia_quiz):
    for player in Player.objects.all():
        score_track = ScoreTracker.objects.get(player_phone=player.phone_number,
                                               session_code=active_trivia_quiz.session_code)

        if not score_track.answered_this_round:
            player.wrong_answers.append((active_trivia_quiz.current_question_index, ''))
            player.save()
            score_track.answered_this_round = True
            score_track.save()
        SMSBot.send('TIME IS UP. NO MORE ANSWERS!', player.phone_number)

    cur_question = TriviaQuestion.objects.get(quiz=active_trivia_quiz.trivia_quiz,
                                                question_index=active_trivia_quiz.current_question_index)
    return render(request, 'activequiz_question.html', {'active_trivia_quiz': active_trivia_quiz, 'cur_question': cur_question})

def question(request, active_trivia_quiz):
    cur_question = TriviaQuestion.objects.get(quiz=active_trivia_quiz.trivia_quiz,
                                              question_index=active_trivia_quiz.current_question_index)
    for player in Player.objects.all():
        score_track = ScoreTracker.objects.get(player_phone=player.phone_number,
                                               session_code=active_trivia_quiz.session_code)
        score_track.answered_this_round = False
        score_track.save()
        SMSBot.send_question(cur_question, player)


    return render(request, 'activequiz_question.html',
                  {'active_trivia_quiz': active_trivia_quiz, 'cur_question': cur_question})


def end_screen(request, active_trivia_quiz):
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

        goodbye = ( f'The session has ended, thanks for playing!\n'
                    f'Team {winner} was the winner!\n'
                    f'Your score was: {score_track.points}/{len(question_set)}'
        )

        SMSBot.send(goodbye, player.phone_number)
        SMSBot.send(player.get_answers(), player.phone_number)
        player.delete()
    return render(request, 'activequiz_end.html',
                  {'active_trivia_quiz': active_trivia_quiz, 'tally_results': tally_results})

@csrf_exempt
def active_trivia(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)

    if request.method == 'POST':
        if 'next-question' in request.POST:
            active_trivia_quiz.current_question_index = active_trivia_quiz.current_question_index + 1
        elif 'show-results' in request.POST:
            active_trivia_quiz.current_question_index = -1
        elif 'times-up' in request.POST:
            return times_up(request, active_trivia_quiz)


    if active_trivia_quiz.current_question_index == 0:
        response = setup(request, active_trivia_quiz)
    elif active_trivia_quiz.current_question_index > 0:
        response = question(request, active_trivia_quiz)
    elif active_trivia_quiz.current_question_index < 0:
        response = end_screen(request, active_trivia_quiz)
    else:
        return HttpResponseNotFound(f"active_trivia_quiz current_question_index "
                                    f"invalid value {active_trivia_quiz.current_question_index}")
    active_trivia_quiz.save()
    return response


class TriviaQuizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ActiveTriviaQuiz
    success_url = '/quiz'

    def test_func(self):
        active_trivia_quiz = self.get_object()
        if self.request.user == active_trivia_quiz.session_master:
            return True
        return False
