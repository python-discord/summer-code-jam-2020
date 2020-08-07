import random
import string

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from trivia_builder.models import TriviaQuiz


class Player(models.Model):
    name = models.CharField(max_length=24)
    number = models.CharField(max_length=12)
    active_quiz = None


class ActiveTriviaQuiz(models.Model):
    trivia_quiz = models.ForeignKey(TriviaQuiz, on_delete=models.CASCADE)
    session_code_val = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    session_code = models.CharField(max_length=6, unique=True, default=session_code_val, editable=False)
    current_question_index = models.IntegerField(default=0)
    session_master = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_master')
    start_time = models.DateTimeField(default=timezone.now)
    players = models.ManyToManyField(Player, related_name='quiz_players')
