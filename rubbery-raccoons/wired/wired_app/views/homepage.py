from django.utils import timezone
from django.views.generic import ListView, ArchiveIndexView
from wired_app.models import Article


class HomepageView(ListView, ArchiveIndexView):
    model = Article
    date_field = "publication_date"
    make_object_list = True
    paginate_by = 10
    template_name = "wired_app/homepage.html"
    context_object_name = "articles"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        years = list(set([a.publication_date.year for a in context["articles"]]))

        years.sort()
        context["years"] = years
        return context
