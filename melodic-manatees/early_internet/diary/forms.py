from django.forms import ModelForm

from diary.models import DiaryEntry


class DiaryEntryForm(ModelForm):

    class Meta:
        model = DiaryEntry
        fields = ("title", "content")
