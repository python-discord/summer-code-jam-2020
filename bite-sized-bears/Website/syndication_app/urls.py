from django.urls import path
from .rss_feed import LatestEntriesFeed

urlpatterns = [
    path('feed/community/<str:username>', LatestEntriesFeed()),
]
