from django.db import models
from django.utils import timezone
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    summary = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    clean_url = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title + " BY " + self.author

    def get_absolute_url(self):
        return reverse("aggregator:Article-detail", kwargs={"pk": self.pk})
