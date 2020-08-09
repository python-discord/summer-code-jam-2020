from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ProfileComment


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class ProfileCommentCreationForm(forms.ModelForm):
    class Meta:
        model = ProfileComment
        fields = ("user_commented_on", "content")
