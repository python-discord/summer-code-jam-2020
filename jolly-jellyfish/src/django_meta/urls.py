"""halfway URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('users/login', auth_views.LoginView.as_view(), name='login'),
    path('users/logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('page_maker.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
