from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import UserPreferences


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Possible ModelForm for updating Preferences
class UserPreferencesForm(ModelForm):

    class Meta:
        model = UserPreferences
        fields = '__all__'
        labels = {
            'weather_preference': "Weather Clothing Suggestions:",
            'name_preference': 'Display Name:'
        }

    def submit_preferences(self):
        pass
