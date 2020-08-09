from django.db import models


class Chatbot(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"name={self.name}"


class WikiArticle(models.Model):
    name = models.CharField(max_length=500)
    summary = models.TextField(max_length=100)
    full_page = models.TextField(max_length=500)

    def __str__(self):
        return f"name={self.name} summary={self.summary}"
