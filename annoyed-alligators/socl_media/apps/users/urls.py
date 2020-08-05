from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', auth_views.LogoutView, name="logout")
]
