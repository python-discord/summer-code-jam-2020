from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from trivia_builder.models import TriviaQuiz


class UserTriviaQuizListView(ListView):
    model = TriviaQuiz
    template_name = 'trivia_hub/user_quizzes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'TriviaQuiz'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return TriviaQuiz.objects.filter(author=user).order_by('-date_posted')


class TriviaQuizDetailView(DetailView):
    model = TriviaQuiz


class TriviaQuizCreateView(LoginRequiredMixin, CreateView):
    model = TriviaQuiz
    fields = ['name', 'questions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TriviaQuizUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TriviaQuiz
    fields = ['name', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        trivia_quiz = self.get_object()
        if self.request.user == trivia_quiz.author:
            return True
        return False


class TriviaQuizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TriviaQuiz
    success_url = '/'

    def test_func(self):
        trivia_quiz = self.get_object()
        if self.request.user == trivia_quiz.author:
            return True
        return False
