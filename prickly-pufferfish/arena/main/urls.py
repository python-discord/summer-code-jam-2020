from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='main/about.html'), name='about'),
    path('battle/', TemplateView.as_view(template_name='battle/battle.html'), name='battle'),


]
