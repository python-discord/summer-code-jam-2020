from django.db import models


class SearchResult(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    htmlTitle = models.CharField(max_length=125)
    link = models.CharField(max_length=150)
    snippet = models.CharField(max_length=300)

    def __repr__(self):
        return f"<id={str(self.id)!r} title={self.title!r} htmlTitle={self.htmlTitle!r} link={self.link!r} \
snippet={self.snippet!r}>"


class Search(models.Model):
    query = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    results = models.ManyToManyField(SearchResult, related_name="search", through='SearchMeta')

    def __repr__(self):
        return f"<query={self.query!r} created_at={str(self.created_at)!r}>"


class SearchMeta(models.Model):
    result = models.ForeignKey(SearchResult, on_delete=models.CASCADE)
    search = models.ForeignKey(Search, on_delete=models.CASCADE)
    page = models.IntegerField()

    def __repr__(self):
        return f"<page={self.page!r}>"
