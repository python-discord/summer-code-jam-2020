from django.views.generic.dates import YearArchiveView

from wired_app.models import Article


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "publication_date"
    make_object_list = True
    