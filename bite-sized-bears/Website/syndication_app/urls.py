from django.urls import path
from syndication_app.rss_feeds import LatestEntriesFeed

urlpatterns = [
    path('feed/community/<str:username>', LatestEntriesFeed()),
]
