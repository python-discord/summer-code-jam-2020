from django.urls import path
from django.conf.urls import url
from .rss_feed import LatestEntriesFeed
from .views import IndexListView

urlpatterns = [
    path('', IndexListView.as_view()),
    path('feed/community/<str:username>', LatestEntriesFeed()),
    # url(r^'/test/', )
]
