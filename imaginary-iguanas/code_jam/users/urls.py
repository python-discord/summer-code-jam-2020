from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as users_views


urlpatterns = [
    path('', users_views.home, name='home'),
    path('users/', users_views.users, name='users'),
    path('signup/', users_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('settings/', users_views.user_settings, name='user-settings'),
    path('updatepassword/', users_views.user_password_update, name='user-password-update')
]
