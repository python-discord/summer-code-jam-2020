from django.urls import path
from . import views

urlpatterns = [
    path("<str:slug>/<int:address>", views.index, name="page"),
]
