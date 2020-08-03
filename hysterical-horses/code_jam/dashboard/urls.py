from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('results/', views.engine_results, name="engine-results")
]
