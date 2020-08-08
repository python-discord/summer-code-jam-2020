from django import forms

from userwall.models import Wall


class WallCreationForm(forms.ModelForm):
    # your_name = forms.CharField(label="Your name", max_length=100)
    #
    class Meta:
        model = Wall
        fields = ["name"]
