from django import forms
from django.db import models

from pp_site.utils.models import TimeStampMixin


class MediaFile(models.Model):
    data = models.FileField()
    is_video = models.BooleanField()


class ForumPost(TimeStampMixin):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    media_file = models.ForeignKey(MediaFile, on_delete=models.CASCADE, blank=True, null=True)


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ["title", "author", "description", "media_file"]


class ForumPostReply(TimeStampMixin):
    author = models.CharField(max_length=30)
    content = models.TextField()
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)


class ForumPostReplyForm(forms.ModelForm):
    class Meta:
        model = ForumPostReply
        fields = ["author", "content"]

