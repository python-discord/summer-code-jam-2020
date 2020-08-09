from django import forms
from django.contrib.auth.forms import PasswordChangeForm as _PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .models import Profile as _Profile


class UserUpdateForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
                                strip=False,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                strip=False,
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
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = _Profile
        fields = ['image', 'gender', 'country', 'place', 'date_of_birth']


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = _Profile
        fields = ['image', 'gender', 'country', 'place', 'date_of_birth', 'audio_track', 'custom_css']
