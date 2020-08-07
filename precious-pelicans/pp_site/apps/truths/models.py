from django import forms
from django.db import models

from pp_site.utils.models import TimeStampMixin
from pp_site.apps.forum.models import ForumMedia

# Create your models here.


class Truth(TimeStampMixin):
    white = 'ffffff'
    red = 'ff0000'
    blue = '3a3aee'
    grey = '9e9e9e'
    yellow = 'ffcc00'
    pink = 'd24dff'
    colors = [(pink, 'Pink'), (white, 'White'), (red, 'Red'), (blue, 'Blue'),
              (grey, 'Grey'), (yellow, 'Yellow')]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = ForumMedia()
    content = models.TextField()
    background_color = models.CharField(max_length=20, choices=colors, default=grey)
    likes = models.IntegerField(default=0)


class TruthReply(TimeStampMixin):
    truth_paper = models.ForeignKey(Truth, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    like = models.IntegerField(default=0)


class TruthUploadForm(forms.ModelForm):
    class Meta:
        model = Truth
        fields = ["title", "author", "content", "cover", "background_color"]
