from django.views.generic import ListView

from trivia_builder.models import TriviaQuiz
from trivia_runner.models import ActiveTriviaQuiz


class ActiveTriviaQuizListView(ListView):
    model = ActiveTriviaQuiz
    template_name = 'trivia_hub/home.html'
    context_object_name = 'active_quizzes'
    ordering = ['-start_time']
    paginate_by = 10


class TriviaQuizListView(ListView):
    model = TriviaQuiz
    template_name = 'trivia_hub/quiz_list.html'
    context_object_name = 'quizzes'
    paginate_by = 10
