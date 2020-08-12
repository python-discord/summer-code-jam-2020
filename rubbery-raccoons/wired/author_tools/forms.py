from django.forms import ModelForm
from wired_app.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "headline", "body", "category"]
