from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Built-in admin page.
    path('admin/', admin.site.urls),

    # Other app pages.
    path('web_portal', include('web_portal.urls', namespace='web_portal')),
    path('ninetys_blog', include('ninetys_blog.urls', namespace='ninetys_blog')),
    path('first_google', include('first_google.urls', namespace='first_google')),
    path('first_youtube', include('first_youtube.urls', namespace='first_youtube')),

    # Twitter page.
    path('first-twitter/', include('first_twitter.urls', namespace='first_twitter')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)