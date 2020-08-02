from django.views.generic import ListView

from trivia_builder.models import TriviaQuiz


class TriviaQuizListView(ListView):
    model = TriviaQuiz
    template_name = 'trivia_hub/home.html'
    context_object_name = 'trivia_quiz'
    ordering = ['-date_posted']
    paginate_by = 10
