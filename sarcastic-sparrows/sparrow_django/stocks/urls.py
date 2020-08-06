from django.urls import path

from . import views


app_name = 'stocks'
urlpatterns = [
    path(" ", views.IndexView, name='index'),
]