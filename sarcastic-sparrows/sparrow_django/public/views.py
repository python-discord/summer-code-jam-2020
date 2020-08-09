from django.http import HttpResponse
from django.views import generic

from public.models import Stock


def stock(request, stock_ticker):
    """
    An example/debug view for printing the data from a particular stock
    TODO: delete before codejam submission
    :param request: The HttpRequest
    :param stock_ticker: the ticker value to be displayed
    :return: An HttpResponse containing the raw QuerySet
    """
    stock_list = Stock.objects.filter(ticker_symbol=stock_ticker)
    return HttpResponse(stock_list)


class IndexView(generic.ListView):
    """
    lists all stocks
    """

    model = Stock
    paginate_by = 10
    template_name = "stock_index.html"
    context_object_name = "stock_index"
    queryset = Stock.objects.filter(ticker_symbol="ebay")
