from django import forms

class Guestbook(forms.Form):
   name = forms.CharField(max_length = 100)
   email = forms.EmailField()
   text = forms.CharField()