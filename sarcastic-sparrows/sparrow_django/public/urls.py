from django.urls import path
from . import views

app_name = "public"
urlpatterns = [path("<stock_ticker>", views.stock, name="stock")]
