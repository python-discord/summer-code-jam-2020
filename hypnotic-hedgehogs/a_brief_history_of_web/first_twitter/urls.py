from django.urls import path
from .views import HomePageView

app_name = 'first_twitter'

urlpatterns = [
    path('', HomePageView.as_view(), name='index')
]