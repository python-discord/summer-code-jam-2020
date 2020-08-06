from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'(?P<battle_id>[a-zA-Z0-9-]+)/$', consumers.ChatConsumer),
]
