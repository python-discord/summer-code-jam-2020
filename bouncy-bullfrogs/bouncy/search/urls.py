from django.urls import path
from . import views
from .views import SearchResultsView
app_name = 'search'

urlpatterns = [
    path("", views.home, name="home"),
    path("process", views.search_process, name="search-process"),
    path("results/<str:query>", SearchResultsView.as_view(),
         name="search-results"),
]
