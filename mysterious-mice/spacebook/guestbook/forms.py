from django import forms


class Guestbook(forms.Form):
    author = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField()
