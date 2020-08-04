from django import forms
from .models import MusicFile


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = MusicFile
        fields = ('music_musicfile', 'music_title')
        widgets = {
            'required': True
        }
