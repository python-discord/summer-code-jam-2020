from django import forms

from chat.models import Room


class RoomCreationForm(forms.ModelForm):
    # your_name = forms.CharField(label="Your name", max_length=100)
    #
    class Meta:
        model = Room
        fields = ["name"]
