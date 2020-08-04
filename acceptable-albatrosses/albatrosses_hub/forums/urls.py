from django.urls import path
from . import views

urlpatterns = [
    path("", views.forumspage, name='forums-home'),
]
