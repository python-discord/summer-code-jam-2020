from django.db import models
from django.contrib.auth.models import User


class TodoEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {'finished' if self.done else 'unfinished'}"
