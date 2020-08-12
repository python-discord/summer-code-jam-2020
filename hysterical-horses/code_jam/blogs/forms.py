from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class CreatePostForm(forms.ModelForm):

    title = forms.CharField(max_length=300, label="Title", widget=forms.TextInput())

    content = forms.CharField(label="Content", widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ("title", "content")
