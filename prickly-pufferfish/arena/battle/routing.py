from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'(?P<battle_id>\d+)/$', consumers.BattleConsumer),
]
