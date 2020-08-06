from django.urls import path, include
from . import views

app_name = "public"
urlpatterns = [
    # Ex: stock/ebay, or, stock/amzn
    path("<stock_ticker>", views.stock, name="stock"),
    path("stocks/", include('sparrow_django.stocks.urls')),

]
