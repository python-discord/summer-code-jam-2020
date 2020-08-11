from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='earlydating-home'),
    path('about/', views.about, name='earlydating-about'),
    path('login/', views.login_page, name='earlydating-login'),
    path('logout/', views.logoutUser, name="earlydating-logout"),
    path('register/', views.register_page, name='earlydating-register'),
    path('YourProfile/', views.your_profile, name='earlydating-yourprofile'),
    path('profile/<str:pk>', views.profile, name='earlydating-profile'),
    path('edit_profile/', views.editprofile, name='earlydating-editprofile'),
    path('DateMatcher/', views.DateMatcher, name='earlydating-DateMatcher'),
    path('mylikes/', views.likedmatches, name='earlydating-mylikes'),
    path('bothlikes/', views.bothliked, name='earlydating-bothlikes')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
