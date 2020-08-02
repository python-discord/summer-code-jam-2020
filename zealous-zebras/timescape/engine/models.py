from django.db import models


class SearchResult(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=50)
    htmlTitle = models.CharField(max_length=75)
    link = models.CharField(max_length=150)
    snippets = models.CharField(max_length=300)

    def __repr__(self):
        return f"<{str(self.id)} {self.title} {self.htmlTitle} {self.link} {self.snippets}>"


class Search(models.Model):
    query = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    results = models.ManyToManyField(SearchResult, related_name="search")

    def __repr__(self):
        return f"<{self.query} {str(self.created_at)}>"
