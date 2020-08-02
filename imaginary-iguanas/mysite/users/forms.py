from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class MySiteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = (
            'username',
            'email',
            'gender',
            'country',
            'city',
            'date_of_birth')  # It needs to be formatted exactly this way, otherwise an Exception will be thrown



