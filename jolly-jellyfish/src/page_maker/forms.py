from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Comment, Webpage, Template, User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'content']


class WebpageForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = [
            'name', 'template_used', 'user_title',
            'user_text_1', 'user_text_2', 'user_text_3',
            'user_image_1', 'user_image_2', 'user_image_3'
        ]


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'style_sheet']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
