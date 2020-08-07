from django import forms


class PostSearchForm(forms.Form):
    search_string = forms.CharField(label="Search:", max_length=100)
