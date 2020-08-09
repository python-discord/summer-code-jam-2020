from django.urls import path

from . import views as wired_views

urlpatterns = [
    path("article/<slug:slug>/", wired_views.detail.article_detail_view, name="article-detail"),
    path(
        "category/<str:category>", wired_views.category.CategoryView.as_view(), name="category-view"
    ),
    path("search", wired_views.search.SearchResultsView.as_view(), name="search-results"),
    path(
        "<int:year>/",
        wired_views.articleyear.ArticleYearArchiveView.as_view(),
        name="article-archive-year",
    ),
    path("", wired_views.homepage.HomepageView.as_view(), name="homepage"),
]
