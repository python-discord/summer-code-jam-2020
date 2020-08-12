from django.db import models
from users.models import Account


class Message(models.Model):
    """
    Model for messages in instant messenger
    """

    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="messages"
    )
    content = models.CharField(max_length=250, blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.content) <= 15:
            title = self.content
        else:
            title = self.content[:15]

        return f"{self.author}: {title}"


class Search(models.Model):
    """
    Model for saving searches from search engine
    """

    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="searches"
    )
    content = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} | {self.content}"

    def save(self, *args, **kwargs):
        check_objects = Search.objects.filter(author=self.author, content=self.content)
        if self.content != "CERN" and self.content not in [
            x.content for x in check_objects
        ]:
            super(Search, self).save(*args, **kwargs)
            self.save()
