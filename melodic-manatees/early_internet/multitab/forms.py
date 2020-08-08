from django import forms
from .models import MultiTab


class TabUploadForm(forms.ModelForm):
    class Meta:
        model = MultiTab
        fields = ('title', 'tab_one', 'tab_two', 'tab_three')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'set title'}),
            'tab_one': forms.TextInput(attrs={'placeholder': 'link one'}),
            'tab_two': forms.TextInput(attrs={'placeholder': 'link two'}),
            'tab_three': forms.TextInput(attrs={'placeholder': 'link three'}),
        }
