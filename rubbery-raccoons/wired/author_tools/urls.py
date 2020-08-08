from django.urls import path

from . import views as at_views

urlpatterns = [
    path("compose", at_views.compose, name="compose"),
]
