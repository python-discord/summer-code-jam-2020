from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserProfile


class MySiteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserProfile
        fields = (
            'username',
            'email',
            'gender',
            'country',
            'city',
            'date_of_birth')  # It needs to be formatted exactly this way, otherwise an Exception will be thrown


class MySiteUserProfileSettingsForm(forms.ModelForm):
    email = forms.EmailField()
    image = forms.ImageField()
    audio_track = forms.FileField()

    class Meta:
        model = UserProfile
        fields = (
            'username',
            'email',
            'image',
            'gender',
            'country',
            'city',
            'date_of_birth',
            'audio_track'
        )
