# from django import forms

from django.forms import ModelForm
from django.contrib.auth.models import User#, Group
from django.contrib.auth.forms import UserCreationForm
from users.models import Team


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class TeamRegistrationForm(ModelForm):
    class Meta:
        model = Team
        fields = ["name", "description"]
