from django.urls import path
from main.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
