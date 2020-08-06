from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r"^$", views.homepage.HomepageView.as_view(), name="homepage"),
    re_path(r'^article/(?P<slug>[\w\-]+)/$', views.detail.ArticleDetailView.as_view(), name="article_detail"),
    
]
