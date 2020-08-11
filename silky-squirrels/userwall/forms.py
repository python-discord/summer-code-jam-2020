from django import forms

# from users.models import User


class WallCreationForm(forms.Form):
    # your_name = forms.CharField(label="Your name", max_length=100)
    username = forms.CharField()
