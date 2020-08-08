from django.urls import path, re_path
from django.conf.urls import url
from .rss_feed import LatestEntriesFeed
from .views import IndexListView, PostView, LoginView, logout_request, SignupView, CommunityView, CommunityListView, UserView\
    , UserProfileUpdate, subscription_request, MyCommunityListView, MostViewedPost, add_comment

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', IndexListView.as_view()),
    path('rss/feed/community/<str:username>', LatestEntriesFeed()),
    path('community/<str:community_name>/<int:post_id>/comment', add_comment),
    re_path(r'^community/(?P<community_name>[-\w_]+)/(?P<post_id>[0-9])/', PostView.as_view()),
    re_path(r'^community/(?P<community_name>[-\w_]+)/$', CommunityView.as_view()),
    re_path(r'^community/(?P<community_name>[-\w_]+)/subscribe/', subscription_request),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^logout', logout_request, name="logout"),
    url(r'^signup', SignupView.as_view(), name="signup"),
    url(r'^top-communities', CommunityListView.as_view(), name="top-communities"),
    url('my-communities/', MyCommunityListView.as_view(),
        name="my-communities"),
    path('user/<int:pk>', UserProfileUpdate.as_view(), name="user-profile"),
    path('user/<str:username>/posts', UserView.as_view()),
    path('most-viewed-posts/', MostViewedPost.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)