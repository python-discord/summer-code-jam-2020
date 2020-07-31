from django.db import models


class MediaFile (models.Model):
    data = models.FileField()
    isVideo = models.BooleanField()


class ForumPostOriginal (models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    author = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    content = models.ForeignKey(MediaFile, on_delete=models.CASCADE)


class ForumPostReply (models.Model):
    date = models.DateTimeField()
    author = models.CharField(max_length=30)
    content = models.TextField()
    topic = models.ForeignKey(ForumPostOriginal, on_delete=models.CASCADE)
