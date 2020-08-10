from django.db.models import Q
from django.views.generic.list import ListView
from wired_app.models import Article


class SearchResultsView(ListView):
    model = Article
    paginate_by = 10
    template_name = "wired_app/search_results.html"
    context_object_name = "articles"

    def get_queryset(self):
        search_text = self.request.GET.get("search-field")
        return Article.objects.filter(
            Q(body__icontains=search_text)
            | Q(title__icontains=search_text)
            | Q(headline__icontains=search_text)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_text = self.request.GET.get("search-field")
        context["search_text"] = search_text
        return context
