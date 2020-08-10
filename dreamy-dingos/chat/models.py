from django.db import models
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SimpleUser(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=50, primary_key=True)
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Message(models.Model):
    objects = models.Manager()
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self._format_short_text(self.text)

    @staticmethod
    def _format_short_text(text: str) -> str:
        if len(text) <= 30:
            return text
        if text[30] == " ":
            return text
        return " ".join(text[:30].split(" ")[:-1]) + "..."
