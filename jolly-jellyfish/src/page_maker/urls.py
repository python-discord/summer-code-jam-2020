from django.urls import path

from .views import MainView, UserRegister

urlpatterns = [
    path('', MainView.as_view(), name='page-maker-main'),
    path('users/register', UserRegister.as_view(), name='register'),
]