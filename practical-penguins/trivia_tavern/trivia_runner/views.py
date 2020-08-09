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
    SMSBot.player_timeout(active_trivia_quiz)
    return render(request, 'activequiz_question.html', {'active_trivia_quiz': active_trivia_quiz, 'cur_question': cur_question})

def question(request, active_trivia_quiz):
    SMSBot.send_all_questions(active_trivia_quiz)
    return render(request, 'activequiz_question.html',
                  {'active_trivia_quiz': active_trivia_quiz, 'cur_question': cur_question})


def end_screen(request, active_trivia_quiz):
    SMSBot.calculate_results(active_trivia_quiz)
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
