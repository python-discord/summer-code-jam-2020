from django.db import models


class Chatbot(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"name={self.name}"
