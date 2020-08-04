from django.http import HttpResponse
from .models import Stock


def stock(request, stock_ticker):
    """
    An example/debug view for printing the data from a particular stock
    TODO: delete before codejam submission
    :param request: The HttpRequest
    :param stock_ticker: the ticker value to be displayed
    :return: An HttpResponse containing the raw QuerySet
    """
    list = Stock.objects.filter(ticker_symbol=stock_ticker)
    return HttpResponse(list)
