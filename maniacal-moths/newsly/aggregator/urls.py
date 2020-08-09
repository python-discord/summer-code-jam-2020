from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    PoliticsListView,
    TechnologyListView,
    EntertainmentListView,
    NewsListView,
    BusinessListView,
    FinanceListView,
    EconomicsListView,
    SportsListView,
    WorldListView,
)
from . import views

app_name = "aggregator"

urlpatterns = [
    path("", ArticleListView.as_view(), name="aggregator-home"),
    path("Article/<int:pk>", ArticleDetailView.as_view(), name="Article-detail"),
    path("Politics/", PoliticsListView.as_view(), name="politics-home"),
    path("Technology/", TechnologyListView.as_view(), name="technology-home"),
    path("Entertainment/", EntertainmentListView.as_view(), name="entertainment-home"),
    path("News/", NewsListView.as_view(), name="news-home"),
    path("Business/", BusinessListView.as_view(), name="business-home"),
    path("Finance/", FinanceListView.as_view(), name="finance-home"),
    path("Economics/", EconomicsListView.as_view(), name="economics-home"),
    path("Sports/", SportsListView.as_view(), name="sports-home"),
    path("World/", WorldListView.as_view(), name="world-home"),
    path("refreshDatabase", views.refresh_database),
    path("about/", views.about, name="aggregator-about"),
]
