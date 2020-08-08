from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["content"]


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = UpdateProfile
        fields = ["name","dob","about"]
