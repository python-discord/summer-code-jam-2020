from django.utils import timezone
from django.views.generic.list import ListView
from wired_app.models import Article


class HomepageView(ListView):
    model = Article
    paginate_by = 10
    template_name = "wired_app/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
