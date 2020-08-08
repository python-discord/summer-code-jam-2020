from django.urls import path

from . import views as wired_views

urlpatterns = [
    path("article/<slug:slug>/", wired_views.detail.ArticleDetailView.as_view(), name="article-detail"),
    path("", wired_views.homepage.HomepageView.as_view(), name="homepage"),
    path("search", wired_views.search.SearchResultsView.as_view(), name="search-results"),
    path("<int:year>/", wired_views.articleyear.ArticleYearArchiveView.as_view(), name="article-archive-year"),
]
