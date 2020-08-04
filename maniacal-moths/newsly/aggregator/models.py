from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Article-detail', kwargs={'pk': self.pk})