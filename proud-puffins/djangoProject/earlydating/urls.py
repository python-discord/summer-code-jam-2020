from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='earlydating-home'),
    path('register/', views.register_page, name='earlydating-register'),
    path('login/', views.login_page, name='earlydating-login'),
    path('logout/', views.logoutUser, name="earlydating-logout"),
    path('DateMatcher/', views.DateMatcher, name='earlydating-DateMatcher'),
    path('about/', views.about, name='earlydating-about'),
    path('YourProfile/', views.your_profile, name='earlydating-yourprofile')
]
