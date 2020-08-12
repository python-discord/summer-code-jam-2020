from django.urls import path
from . import views

urlpatterns = [
    path("<str:slug>/<int:address>/<str:page>", views.index, name="page"),
]
