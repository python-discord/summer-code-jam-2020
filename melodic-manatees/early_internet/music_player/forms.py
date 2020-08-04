from django import forms
from .models import MusicFile


class FileUploadForm(forms.ModelForm):
    music_musicfile = forms.FileField(
        label='upload track')
    music_title = forms.CharField(
        label='track name')

    class Meta:
        model = MusicFile
        fields = ('music_musicfile', 'music_title')
        widgets = {
            'required': True
        }
