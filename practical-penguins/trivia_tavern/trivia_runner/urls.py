from django.urls import path

from trivia_runner.views import (setup, question, end_screen)

urlpatterns = [
    path('<int:pk>/setup/', setup, name='activequiz-setup'),
    path('<int:pk>/<int:question_number>/', question, name='activequiz-question'),
    path('<int:pk>/end/', end_screen, name='activequiz-end'),
]
