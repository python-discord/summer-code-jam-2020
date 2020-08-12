from django.urls import path
from games.views import make_move

urlpatterns = [
    path('ttt', make_move),
]
