from django.urls import path

from trivia_hub.views import TriviaQuizListView


urlpatterns = [
    path('', TriviaQuizListView.as_view(), name='main_hub'),
]
