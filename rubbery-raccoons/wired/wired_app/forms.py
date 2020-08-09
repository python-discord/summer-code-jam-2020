from django.forms import ModelForm
from wired_app.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
