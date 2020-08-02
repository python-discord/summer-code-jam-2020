from django.urls import path, include
from main.views import HomeView, Register


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', Register.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
