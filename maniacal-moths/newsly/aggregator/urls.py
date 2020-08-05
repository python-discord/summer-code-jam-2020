from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
)
from . import views

urlpatterns = [
    path("", ArticleListView.as_view(), name="aggregator-home"),
    path("Article/<int:pk>/", ArticleDetailView.as_view(), name="Article-detail"),
    path("about/", views.about, name="aggregator-about"),
]
