from django import forms
from .models import BackgroundFile


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = BackgroundFile
        fields = ('background_file', 'background_title')
        widgets = {
            'required': True
        }
