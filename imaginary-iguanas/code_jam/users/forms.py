from django import forms
from django.contrib.auth.forms import UserCreationForm as _UserCreationForm

from .models import Profile as _Profile


class UserUpdateForm(_UserCreationForm):
    pass


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = _Profile
        fields = ['image', 'gender', 'country', 'city', 'date_of_birth']
