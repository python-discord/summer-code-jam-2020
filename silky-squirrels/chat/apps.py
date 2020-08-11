from django.apps import AppConfig
from chat.models import RoomMember


class ChatConfig(AppConfig):
    name = "chat"

    def ready(self):
        RoomMember.objects.all().update(active=False)
