from django.db import models


class HighScore(models.Model):
    initials = models.CharField(max_length=3)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.initials
