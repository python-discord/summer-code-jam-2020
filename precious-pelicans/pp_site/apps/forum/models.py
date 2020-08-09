from django import forms
from django.db import models
from django.forms import Textarea, ValidationError
from django.template.defaultfilters import filesizeformat

from pp_site.utils.models import TimeStampMixin


class ForumMedia(models.FileField):
    image_types = ("image/gif", "image/jpeg", "image/png")
    video_types = ("video/mp4", "video/webm", "video/ogg")

    def __init__(self, *args, **kwargs):
        kwargs["blank"] = True
        kwargs["null"] = True

        self.max_size = kwargs.pop("max_size", 20971520)

        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)

        file = data.file
        content_type = file.content_type

        if content_type in self.image_types or content_type in self.video_types:
            if file.size > self.max_size:
                raise ValidationError(f"Please keep filesize under: {filesizeformat(self.max_size)}")
            return data
        raise ValidationError("Invalid content type")


class ForumPost(TimeStampMixin):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    media_file = ForumMedia()
    rating = models.IntegerField(default=0)
    is_video = models.BooleanField(default=False)


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
        widgets = {
            "content": Textarea(attrs={'width': '100%', 'height': '3em'})
        }
