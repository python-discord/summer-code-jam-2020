from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

from trivia_builder.models import TriviaQuiz


class ActiveTriviaQuiz(models.Model):
    trivia_quiz = models.ForeignKey(TriviaQuiz, on_delete=models.CASCADE)
    session_code = models.PositiveIntegerField(validators=[MaxValueValidator(6)], unique=True)
    current_question_index = models.PositiveIntegerField()
    session_master = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now_add=True)
    players = models.ManyToManyField(User)
