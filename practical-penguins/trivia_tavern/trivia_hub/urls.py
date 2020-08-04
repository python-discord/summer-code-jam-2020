from django.urls import path

from trivia_hub.views import ActiveTriviaQuizListView, TriviaQuizListView

urlpatterns = [
    path('', ActiveTriviaQuizListView.as_view(), name='main_hub'),
    path('quiz/', TriviaQuizListView.as_view(), name='quiz-list'),
]
