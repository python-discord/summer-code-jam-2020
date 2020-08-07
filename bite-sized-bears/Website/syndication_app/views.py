from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

def index(request):
    return HttpResponse("Hello, world. You're at the Syndication index.")


class IndexListView(ListView):
    paginate_by = 25
    template_name = "index.html"
    queryset = Post.objects.all()
