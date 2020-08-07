from django.urls import path, re_path
# from django.conf.urls import url
from .rss_feed import LatestEntriesFeed
from .views import IndexListView, PostView, CommunityView, TopCommunityView

urlpatterns = [
    path('', IndexListView.as_view()),
    path('feed/community/<str:username>', LatestEntriesFeed()),
    path('top-communities/', TopCommunityView.as_view()),
    path('c/<str:community_name>/', CommunityView.as_view()),
    path('c/<str:community_name>/<int:post_id>/', PostView.as_view()),
]
