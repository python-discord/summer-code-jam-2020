from django import forms
from .models import Song


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('song_title', 'song_songfile')
