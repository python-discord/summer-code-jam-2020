from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    post_image = forms.ImageField(required=True)

    class Meta:
        model = Post
        fields = ['post_content', 'post_image']
