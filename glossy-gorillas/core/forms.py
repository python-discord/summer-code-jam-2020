from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import Trader


class UserRegisterForm(UserCreationForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        Trader.objects.create(user=user, description="")
        return user
