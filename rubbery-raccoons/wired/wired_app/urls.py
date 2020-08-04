from django.urls import path

from . import views

urlpatterns = [
    path(
        "article/<slug:slug>/", views.detail.ArticleDetailView.as_view(), name="article-detail"
    ),
    path("author/compose", views.compose, name="wiredapp-compose"),
    path("", views.homepage.HomepageView.as_view(), name="homepage"),
]
