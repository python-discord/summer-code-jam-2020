from django import forms


class PostSearchForm(forms.Form):
    search_string = forms.CharField(label="Search:", max_length=100)


class MediaUploadForm(forms.Form):
    file_label = 'file'
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=30)
    description = forms.CharField(max_length=1000)
    media_file = forms.FileField(label=file_label)
