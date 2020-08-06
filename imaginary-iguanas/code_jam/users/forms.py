from django import forms
from django.contrib.auth.forms import UserCreationForm as _UserCreationForm, PasswordChangeForm as _PasswordChangeForm

from .models import Profile as _Profile


class UserUpdateForm(_UserCreationForm):
    pass


class UserPasswordUpdateForm(_PasswordChangeForm):
    pass


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = _Profile
        fields = ['image', 'gender', 'country', 'city', 'date_of_birth']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = _Profile
        fields = ['image', 'gender', 'country', 'city', 'date_of_birth', 'audio_track', 'profile_css']
