from django.urls import path
from . import views

app_name = "public"
urlpatterns = [
    # Ex: stock/ebay, or, stock/amzn
    path("<stock_ticker>", views.stock, name="stock"),
]
