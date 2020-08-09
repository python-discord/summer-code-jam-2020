"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from anon import views as anon_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('anonuser/', anon_views.test),
    path('auth/', anon_views.get_auth_token, name='get-auth'),
    path('data/', anon_views.get_user_data, name='get-data'),
    re_path(r'^$', serve, kwargs={
        'path': 'index.html', 'document_root': 'www/dist'}),
    re_path(r'^(?P<path>.*)$', serve, {
        'document_root': 'www/dist',
    }),
    path('recent/', anon_views.get_recent, name='get-recent'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
