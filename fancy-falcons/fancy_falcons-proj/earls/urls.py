from django.urls import path
from . import views

app_name = "earls"
urlpatterns = [
    path('', views.earl_list_view, name='earl-list'),
    path('<int:pk>/', views.earl_public_page, name='earldetail'),
]
