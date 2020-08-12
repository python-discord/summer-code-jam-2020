from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Account, Profile


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = UserCreationForm.Meta.fields + ("email",)


class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ["username", "email"]


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["biography", "avatar"]
