import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from users.models import Profile, ChatRoomVisit
from chat.models import RoomMember, Message, Room
from django.utils import timezone


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # noinspection PyAttributeOutsideInit
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # noinspection PyAttributeOutsideInit
        self.room_group_name = "chat_%s" % self.room_name
        self.user = self.scope["user"]
        room = Room.objects.get(name=self.room_name)
        profile = Profile.objects.get(user=self.user)
        ChatRoomVisit.objects.get_or_create(profile=profile, chat_room=room)
        ChatRoomVisit.objects.filter(profile=profile, chat_room=room).update(time_visited=timezone.now())

        self.user = self.scope["user"]
        room = Room.objects.get(name=self.room_name)

        RoomMember.objects.filter(user=self.user, room=room).update(active=True)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        self.accept()

        # Send this user connected to all users
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "username": self.user.username, "connected": True}
        )

    def disconnect(self, close_code):

        self.user = self.scope["user"]
        room = Room.objects.get(name=self.room_name)

        RoomMember.objects.filter(user=self.user, room=room).update(active=False)
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

        # noinspection PyAttributeOutsideInit
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # noinspection PyAttributeOutsideInit
        self.room_group_name = "chat_%s" % self.room_name

        # Send this user connected to all users
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "username": self.user.username, "connected": False}
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        room_member_id = text_data_json["room_member_id"]
        text = text_data_json["text"]
        room_member = RoomMember.objects.get(id=room_member_id)
        message = Message.objects.create(room_member=room_member, room=room_member.room, text=text)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "username": room_member.user.username,
                "text": text,
                "timestamp": str(message.timestamp),
            },
        )

    # Receive message from room group
    def chat_message(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
