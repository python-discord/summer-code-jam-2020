from django.urls import path

from . import views

urlpatterns = [
    path('author/compose', views.compose, name='wiredapp-compose'),
]
