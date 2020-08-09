from django.conf.urls import url
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from .rss_feed import LatestEntriesFeed
from .import views


urlpatterns = [
    path('', views.IndexListView.as_view()),
    path('user/<str:username>/posts', views.UserView.as_view()),
    path('rss/feed/community/<str:username>', LatestEntriesFeed()),
    path('user/<int:pk>', views.UserProfileUpdate.as_view(), name="user-profile"),
    path('community/<str:community_name>/<int:post_id>/comment', views.add_comment),
    path('community/<str:community_name>/post', views.PostCreate.as_view(), name="create-post"),
    path('top-communities/create_community', views.CommunityCreate.as_view(), name="create-community"),

    re_path(r'^community/(?P<community_name>[-\w_]+)/(?P<post_id>[0-9]+)/', views.PostView.as_view()),
    re_path(r'^community/(?P<community_name>[-\w_]+)/$', views.CommunityView.as_view()),
    re_path(r'^community/(?P<community_name>[-\w_]+)/subscribe/', views.subscription_request),

    url(r'^home', views.HomeListView.as_view(), name="home"),
    url(r'^login', views.LoginView.as_view(), name="login"),
    url(r'^logout', views.logout_request, name="logout"),
    url(r'^signup', views.SignupView.as_view(), name="signup"),
    url(r'^top-communities', views.CommunityListView.as_view(), name="top-communities"),
    url(r'^my-communities', views.MyCommunityListView.as_view(), name="my-communities"),
    url(r'^most-viewed-posts', views.MostViewedPost.as_view(), name="most-viewed"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
