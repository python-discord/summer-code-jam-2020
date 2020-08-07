from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView

from trivia_builder.models import TriviaQuestion
from trivia_runner.models import ActiveTriviaQuiz


def setup(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)
    return render(request, 'activequiz_setup.html', {'active_trivia_quiz': active_trivia_quiz})


def question(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)

    question_number = active_trivia_quiz.current_question_index
    cur_question = TriviaQuestion.objects.filter(quiz=active_trivia_quiz.trivia_quiz)[question_number-1]
    # cur_question = active_trivia_quiz.trivia_quiz.triviaquestion_set.all()[question_number:]
    return render(request, 'activequiz_question.html',
                  {'active_trivia_quiz': active_trivia_quiz, 'cur_question': cur_question})


def end_screen(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)
    tally_results = {'winner': "DUMMY USER",
                     'score_list': [("DUMMY USER", 10),
                                    ("DUMMY USER 2", 2),
                                    ("DUMMY USER 3", 1),
                                    ("DUMMY USER 4", 0), ]}
    return render(request, 'activequiz_end.html',
                  {'active_trivia_quiz': active_trivia_quiz, 'tally_results': tally_results})


def active_trivia(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)

    if request.method == 'POST':
        if 'next-question' in request.POST:
            active_trivia_quiz.current_question_index = active_trivia_quiz.current_question_index + 1
        elif 'show-results' in request.POST:
            active_trivia_quiz.current_question_index = -1

    if active_trivia_quiz.current_question_index == 0:
        response = setup(request, pk=active_trivia_quiz.pk)
    elif active_trivia_quiz.current_question_index > 0:
        response = question(request, pk=active_trivia_quiz.pk)
    elif active_trivia_quiz.current_question_index < 0:
        response = end_screen(request, pk=active_trivia_quiz.pk)
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
