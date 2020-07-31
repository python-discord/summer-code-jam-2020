from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('page/home', views.homepage),
    path('', views.homepage)
]
