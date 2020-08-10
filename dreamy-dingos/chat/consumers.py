import datetime
import json
import uuid
from typing import List

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """Connecting to room."""
        self.user_uuid = uuid.uuid4()
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = 'chat_%s' % self.room_id
        self.session_messages: List[Message] = []

        # Join to the room
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()

    def disconnect(self, close_code):
        """Leave the room."""
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

        # Filtering duplicates from different sessions
        # Giving dates specific format to compare them
        messages_in_db = Message.objects.values_list('created_at', flat=True)
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        messages_in_db_dates = [
            datetime.datetime.strftime(item, date_format)
            for item in messages_in_db
        ]
        messages_to_save = list(
            filter(
                lambda message:
                datetime.datetime.strftime(message.created_at, date_format)
                not in messages_in_db_dates,
                self.session_messages,
            )
        )

        Message.objects.bulk_create(messages_to_save)

    def receive(self, text_data):
        """Receive message from websocket."""
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': str(self.user_uuid) + ": " + message,
                'created_at_iso': text_data_json["created_at"],
            },
        )

    def chat_message(self, event):
        """Receive message from room group."""
        message = event["message"]
        created_at = datetime.datetime.strptime(
                    event["created_at_iso"], "%Y-%m-%dT%H:%M:%S.%fZ")

        self.session_messages.append(
            Message(text=message, room_id=self.room_id, created_at=created_at),
        )

        # Send message to Websocket
        self.send(text_data=json.dumps({
            "message": message,
        }))
