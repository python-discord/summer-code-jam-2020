from django import forms

from .models import BlogComment as _BlogComment
from .models import ProfileComment as _ProfileComment


class ProfileCommentForm(forms.ModelForm):
    class Meta:
        model = _ProfileComment
        fields = ['comment']


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = _BlogComment
        fields = ['comment']
