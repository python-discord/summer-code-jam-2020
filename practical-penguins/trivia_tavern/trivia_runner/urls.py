from django.urls import path

from trivia_runner.views import setup, active_trivia, TriviaQuizDeleteView, ActiveTriviaQuizListView

urlpatterns = [
    path('', ActiveTriviaQuizListView.as_view(), name='activequiz-list'),
    path('<int:pk>/', active_trivia, name='activequiz'),
    path('<int:pk>/setup/', setup, name='activequiz-setup'),
    path('<int:pk>/delete/', TriviaQuizDeleteView.as_view(), name='activequiz-delete'),
]
