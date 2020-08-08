from django.forms import ModelForm
from wired_app.models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "headline", "body"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
