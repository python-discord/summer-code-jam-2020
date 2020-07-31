from django.urls import path
from . import views
app_name = 'mail'
urlpatterns = [
    path('signup/', views.signup),
]
