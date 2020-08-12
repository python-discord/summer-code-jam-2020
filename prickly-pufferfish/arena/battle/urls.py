from django.urls import path
from .views import PreBattleView, BattleView

urlpatterns = [
    path('', PreBattleView.as_view(), name='pre_battle'),
    path('<int:pk>/', BattleView.as_view(), name='battle'),
]
