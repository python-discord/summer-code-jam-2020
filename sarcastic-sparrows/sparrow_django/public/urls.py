from django.urls import path
from . import views

app_name = "public"
""" urls should always end with "/", see example at https://docs.djangoproject.com/en/3.0/topics/http/urls/ """
urlpatterns = [
    # Ex: stock/ebay, or, stock/amzn
    path("<stock_ticker>/", views.stock, name="stock"),
    # Ex: stock/index/
    path("<stock_ticker>/index/", views.IndexView, name="index"),
]
