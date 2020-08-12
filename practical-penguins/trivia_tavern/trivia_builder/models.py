from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TriviaQuiz(models.Model):

    name = models.CharField(max_length=30, blank=False,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500,)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'pk': self.pk})


class TriviaQuestion(models.Model):
    question_text = models.CharField(max_length=1000, blank=False,)
    question_answer = models.CharField(max_length=300, blank=False,)
    question_index = models.PositiveIntegerField(blank=False)
    quiz = models.ForeignKey(TriviaQuiz, on_delete=models.CASCADE)
