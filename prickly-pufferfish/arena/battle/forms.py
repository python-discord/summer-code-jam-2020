from django import forms


class BattleForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)
