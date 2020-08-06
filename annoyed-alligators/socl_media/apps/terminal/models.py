from django.db import models

# Create your models here.
class NewsHistory(models.Model):
    user_id = models.IntegerField()
    search_topic = models.CharField(max_length=50)
    search_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_fetched_count = models.IntegerField()
    news_articles = models.TextField()
    
