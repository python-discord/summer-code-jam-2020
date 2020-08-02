from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TriviaQuiz(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'pk': self.pk})


class TriviaQuestion(models.Model):
    question_text = models.CharField(max_length=30)
    question_answer = models.CharField(max_length=30)
    question_type = models.CharField(max_length=30)
    quiz = models.ForeignKey(TriviaQuiz, on_delete=models.CASCADE)

