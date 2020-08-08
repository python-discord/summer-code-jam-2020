from django.urls import path

from . import views as wired_views

urlpatterns = [
<<<<<<< HEAD
    path("article/<slug:slug>/", views.detail.ArticleDetailView.as_view(), name="article-detail"),
    path("", views.homepage.HomepageView.as_view(), name="homepage"),
    path("search", views.search.SearchResultsView.as_view(), name="search-results"),
    path("<int:year>/", views.articleyear.ArticleYearArchiveView.as_view(), name="article-archive-year"),
=======
    path("article/<slug:slug>/", wired_views.detail.ArticleDetailView.as_view(), name="article-detail"),
    path("", wired_views.homepage.HomepageView.as_view(), name="homepage"),
    path("search", wired_views.search.SearchResultsView.as_view(), name="search-results"),
>>>>>>> c3426bb446e5cc55c628903ba456fef8ed1d539e
]
