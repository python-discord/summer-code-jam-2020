from django.forms import ClearableFileInput
from .models import SongData, SongFile


class TitleUploadForm(forms.ModelForm):
    class Meta:
        model = SongData
        fields = ('song_title')

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = SongFile
        fields = ('song_songfile')
        widgets = {
            'song_songfile': ClearableFileInput(attrs={
                'multiple':True,
                'required'=True
                })
            }
