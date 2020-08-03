from django import forms

class Guestbook(forms.Form):
   name = forms.CharField(max_length = 100)
   text = forms.CharField(widget = forms.PasswordInput())