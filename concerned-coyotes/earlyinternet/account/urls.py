from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name="login.html",
        extra_context={'next': '/'},
        redirect_authenticated_user=True
    ),
         name="login"),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
