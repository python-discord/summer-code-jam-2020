from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index)
]
