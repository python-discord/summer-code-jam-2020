from django.urls import path

from . import views
from .views import DashboardView

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
]
