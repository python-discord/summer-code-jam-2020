from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:user_id>/', views.user, name='users-id'),
    path('', views.home, name="users-home"),
]
