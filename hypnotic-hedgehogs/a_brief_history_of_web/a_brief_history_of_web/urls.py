from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='main-page'),
    path('admin/', admin.site.urls),
    path('web_portal', include('web_portal.urls', namespace='web_portal')),
    path('ninetys_blog', include('ninetys_blog.urls', namespace='ninetys_blog')),
    path('first_google', include('first_google.urls', namespace='first_google')),
    path('first_twitter', include('first_twitter.urls', namespace='first_twitter')),
    path('first_youtube', include('first_youtube.urls', namespace='first_youtube')),
]
