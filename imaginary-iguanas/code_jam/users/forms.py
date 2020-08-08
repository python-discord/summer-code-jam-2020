from django import forms
from django.contrib.auth.forms import PasswordChangeForm as _PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .models import Profile as _Profile


class UserUpdateForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = ("username",)
        help_texts = {
            'username': None
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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
