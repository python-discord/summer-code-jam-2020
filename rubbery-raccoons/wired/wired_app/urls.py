from django.urls import path

from . import views as wired_views

urlpatterns = [
    path("article/<slug:slug>/", views.detail.ArticleDetailView.as_view(), name="article-detail"),
    path("", views.homepage.HomepageView.as_view(), name="homepage"),
    path("search", views.search.SearchResultsView.as_view(), name="search-results"),
    path("<int:year>/", views.articleyear.ArticleYearArchiveView.as_view(), name="article-archive-year"),
]
