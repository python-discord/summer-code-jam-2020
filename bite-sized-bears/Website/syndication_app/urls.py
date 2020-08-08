from django.urls import path, re_path
from django.conf.urls import url
from .rss_feed import LatestEntriesFeed
from .views import IndexListView, PostView, LoginView, logout_request, SignupView, CommunityView, TopCommunityView


urlpatterns = [
    path('', IndexListView.as_view()),
    path('rss/feed/community/<str:username>', LatestEntriesFeed()),
    re_path(r'^community/(?P<community_name>[\w+-_])/(?P<post_id>[0-9])', PostView.as_view()),
    re_path(r'^community/(?P<community_name>\w+)', CommunityView.as_view()),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^logout', logout_request, name="logout"),
    url(r'^signup', SignupView.as_view(), name="signup"),
    url(r'^top-communities', TopCommunityView.as_view(), name="top-communities"),

]
