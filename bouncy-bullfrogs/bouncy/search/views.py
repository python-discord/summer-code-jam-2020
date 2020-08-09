from django.shortcuts import render, reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView
from .models import Result
from django.db.models import Q
# Create your views here.


def home(request):
    return render(request, "search/home.html")


class SearchResultsView(ListView):
    template_name = "search/search_results.html"
    context_object_name = "results_list"
    paginate_by = 10

    def get_queryset(self, **kwargs):
        query = self.kwargs['query']
        print(f"query is {query}")
        results = Result.objects.filter(Q(title__icontains=query) | Q(
            snippet__icontains=query) | Q(link__icontains=query))
        return results


def search_process(request):
    if request.method == 'POST':
        query = request.POST.get('q', None)
        return HttpResponseRedirect(reverse("search:search-results",
                                            kwargs={'query': query}))
