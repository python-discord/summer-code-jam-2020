from django.urls import path
from . import views
from .views import UserEditView

urlpatterns = [
    path('', views.home, name='earlydating-home'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('register/', views.register_page, name='earlydating-register'),
    path('login/', views.login_page, name='earlydating-login'),
    path('logout/', views.logoutUser, name="earlydating-logout"),
    path('DateMatcher/', views.DateMatcher, name='earlydating-DateMatcher'),
    path('about/', views.about, name='earlydating-about'),
    path('YourProfile/', views.your_profile, name='earlydating-yourprofile')
]
