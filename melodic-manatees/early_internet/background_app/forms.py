from django import forms
from .models import BackgroundFile
from .background_utility import file_size


class FileUploadForm(forms.ModelForm):
    '''Background image upload form'''
    background_file = forms.FileField(
        label='upload background',
        validators=[file_size],
        required=True,
    )

    class Meta:
        model = BackgroundFile
        fields = ('background_file', 'background_title')
        widgets = {
            'required': True
        }
