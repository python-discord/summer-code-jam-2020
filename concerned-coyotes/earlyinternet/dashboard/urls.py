from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update-location', views.update_location, name='update_location'),
]
