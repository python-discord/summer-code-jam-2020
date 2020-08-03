from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='earlydating-home'),
    path('DateMatcher/', views.DateMatcher, name='earlydating-DateMatcher'),
    path('about/', views.about, name='earlydating-about'),
    path('YourProfile/<str:pk>/', views.your_profile, name='earlydating-yourprofile')
]
