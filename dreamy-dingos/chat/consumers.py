import json
import uuid

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """Connecting to room."""
        self.user_uuid = uuid.uuid4()
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = 'chat_{0}'.format(self.room_name)

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
            self.channel_layer,
        )

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
            },
        )
    
    def chat_message(self, event):
        """Receive message from room group."""
        message = event["message"]

        # Send message to Websocket
        self.send(text_data=json.dumps({
            "message": message,
        }))
