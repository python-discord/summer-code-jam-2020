from django.urls import path, include
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('welcome', views.index, name='index'),

]
