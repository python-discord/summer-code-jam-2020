from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main-home'),
    path('about/', views.about, name='main-about')

]
