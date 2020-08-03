import requests
from django.http import HttpResponse


def stock(request, stock_ticker):
    r = requests.get(
        "https://raw.githubusercontent.com/rdcox/dotcom-data/master/txt/"
        + str(stock_ticker)
        + ".us.txt"
    )
    return HttpResponse(r.content)
