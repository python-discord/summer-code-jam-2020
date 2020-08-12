from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import CustomUser, Topic, Post


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15)
    password = forms.CharField(label="Password", max_length=25)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")


class TopicCreationForm(forms.Form):
    name = forms.CharField(label="Topic Name", max_length=20)


class PostForm(forms.ModelForm):
    title = forms.CharField(label="Title", widget=forms.TextInput(), max_length=30)
    body = forms.CharField(label="Body", widget=forms.Textarea())
    topic = forms.ModelChoiceField(label="Topic", queryset=Topic.objects.all())

    class Meta:
        model = Post
        fields = ("title", "body", "topic")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_img', 'username', 'bio')
