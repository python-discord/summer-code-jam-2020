from django.urls import path, re_path
from django.conf.urls import url
from .rss_feed import LatestEntriesFeed
from .views import IndexListView, PostView, LoginView, logout_request, SignupView

urlpatterns = [
    path('', IndexListView.as_view()),
    path('feed/community/<str:username>', LatestEntriesFeed()),
    path('c/<str:community_name>/<int:post_id>/', PostView.as_view()),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^logout', logout_request, name="logout"),
    url(r'^signup', SignupView.as_view(), name="signup"),
]
