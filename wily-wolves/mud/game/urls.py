from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'game'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='game/login.html'), name='login'),
]
