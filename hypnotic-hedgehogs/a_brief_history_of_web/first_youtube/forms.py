from django.forms import ModelForm, Textarea
from django import forms
from .models import Comment


class CommentForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'style':'width:450px;height:100px'
        }
    ), label='')
    class Meta:
        model = Comment
        fields = ['content']



