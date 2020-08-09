from django.db import models


class NewsHistory(models.Model):
    """
    This model will temporarily store the news fetched to allow
    followup response.
    """

    user_id = models.IntegerField()
    search_topic = models.CharField(max_length=50)
    search_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_fetched_count = models.IntegerField()
    news_articles = models.TextField()

    def __str__(self):
        return f'user={self.user_id!r} topic={self.search_topic!r} time={self.search_time!r}'
