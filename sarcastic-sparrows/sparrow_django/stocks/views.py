from django.shortcuts import render
from django.views import generic

import sparrow_django.public.models


class IndexView(generic.ListView):
    """
    lists all stocks
    """
    model = Stock
    paginate_by = 10
    template_name = 'stocks/index.html'
    context_object_name = 'index'
    queryset = Stock.objects.all()
