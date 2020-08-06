from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView

from trivia_runner.models import ActiveTriviaQuiz


def setup(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)
    return render(request, 'activequiz_setup.html', {'active_trivia_quiz': active_trivia_quiz})


def question(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)

    question_number = active_trivia_quiz.current_question_index
    cur_question = active_trivia_quiz.trivia_quiz.triviaquestion_set[question_number]
    return render(request, 'activequiz_question.html',
                  {'active_trivia_quiz': active_trivia_quiz, 'cur_question': cur_question})


def active_trivia(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)

    if request.method == 'POST':
        if 'next-question' in request.POST:
            active_trivia_quiz.current_question_index = active_trivia_quiz.current_question_index + 1
            active_trivia_quiz.save()
            return redirect("activequiz", pk=active_trivia_quiz.pk)
        elif 'show-results' in request.POST:
            active_trivia_quiz.current_question_index = -1
            active_trivia_quiz.save()
            return redirect("activequiz", pk=active_trivia_quiz.pk)
        elif 'end-quiz' in request.POST:
            return redirect("activequiz-delete", pk=active_trivia_quiz.pk)

    if active_trivia_quiz.current_question_index == 0:
        return redirect('activequiz-setup', pk=active_trivia_quiz.pk)
    elif active_trivia_quiz.current_question_index > 0:
        return redirect('activequiz-question', pk=active_trivia_quiz.pk)
    elif active_trivia_quiz.current_question_index < 0:
        return redirect('activequiz-end', pk=active_trivia_quiz.pk)
    else:
        return HttpResponseNotFound(f"active_trivia_quiz current_question_index "
                                    f"invalid value {active_trivia_quiz.current_question_index}")


class TriviaQuizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ActiveTriviaQuiz
    success_url = '/quiz'

    def test_func(self):
        trivia_quiz = self.get_object()
        if self.request.user == trivia_quiz.author:
            return True
        return False


def end_screen(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)
    tally_results = {'winner': "DUMMY USER",
                     'score_list': [("DUMMY USER", 10),
                                    ("DUMMY USER 2", 2),
                                    ("DUMMY USER 3", 1),
                                    ("DUMMY USER 4", 0), ]}
    return render(request, 'activequiz_end.html',
                  {'active_trivia_quiz': active_trivia_quiz, 'tally_results': tally_results})
    pass
