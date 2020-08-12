from django.urls import path
from . import views

app_name = 'earlcal'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/<int:event_id>/', views.event_view, name='event_view'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
]
