from django.urls import path
from . import views

app_name = 'first_google'
urlpatterns = [
    path('', views.index, name='index'),
    path('/results/<str:search_text>', views.results, name='results')
]
