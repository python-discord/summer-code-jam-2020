from django import forms
from django.contrib.auth.forms import UserCreationForm as _UserCreationForm

from .models import Profile


class UserCreateForm(_UserCreationForm):
    pass


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'gender', 'country', 'city', 'date_of_birth']
