from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .news_api_choices import NEWS_API_SOURCE_CHOICES

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    news_api_source = forms.ChoiceField(choices=NEWS_API_SOURCE_CHOICES)

    class Meta:
        model = User
        fields = ["username", "email",'news_api_source', "password1", "password2"]
