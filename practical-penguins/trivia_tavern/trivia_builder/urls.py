from django.urls import path

from trivia_builder.views import (TriviaQuizDeleteView,
                                  TriviaQuizUpdateView,
                                  TriviaQuizCreateView,
                                  TriviaQuizDetailView,
                                  UserTriviaQuizListView)

urlpatterns = [
    path('user/<str:username>/', UserTriviaQuizListView.as_view(), name='user-quizzes'),
    path('id/<int:pk>/', TriviaQuizDetailView.as_view(), name='quiz-detail'),
    path('new/', TriviaQuizCreateView.as_view(), name='quiz-create'),
    path('<int:pk>/update/', TriviaQuizUpdateView.as_view(), name='quiz-update'),
    path('<int:pk>/delete/', TriviaQuizDeleteView.as_view(), name='quiz-delete'),
]
