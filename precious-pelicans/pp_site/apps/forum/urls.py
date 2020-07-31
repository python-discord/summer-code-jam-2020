from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:PostId>/', views.post, name='viewpost'),
    path('', views.index, name='home')
]
