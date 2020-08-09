from django.urls import path

from . import views

urlpatterns = [
    path('', views.earl_list_view, name='earl-list'),
]