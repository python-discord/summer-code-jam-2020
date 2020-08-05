from django.shortcuts import render, get_object_or_404

from trivia_runner.models import ActiveTriviaQuiz


def setup(request, pk):
    active_trivia_quiz = get_object_or_404(ActiveTriviaQuiz, pk=pk)
    return render(request, 'activequiz_setup.html', {'active_trivia_quiz': active_trivia_quiz})


def question(request):
    pass


def end_screen(request):
    pass
