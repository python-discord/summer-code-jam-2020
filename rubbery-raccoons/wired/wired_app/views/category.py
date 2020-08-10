from django.views.generic.list import ListView
from wired_app.models import Article


class CategoryView(ListView):
    model = Article
    paginate_by = 10
    template_name = "wired_app/category.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs["category"]).order_by("-created")

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        category = self.kwargs["category"]
        if category == "general":
            category_title = "General News"
        else:
            category_title = category[0].upper() + category[1:]
            category_title = "Articles on " + category_title
        context["category_title"] = category_title

        years = list(set([a.publication_date.year for a in context["articles"]]))
        years.sort()
        context["years"] = years

        return context
