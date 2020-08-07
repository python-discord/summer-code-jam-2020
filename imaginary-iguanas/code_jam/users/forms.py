from django import forms
from django.contrib.auth.forms import PasswordChangeForm as _PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .models import Profile as _Profile


class UserUpdateForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False
    )

    class Meta:
        model = User
        fields = ("username",)
        help_texts = {
            'username': None
        }


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