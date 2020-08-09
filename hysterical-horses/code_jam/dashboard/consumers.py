import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """
    consumer for chat room, connects chat room to Redis to connect chats to each other
    """

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        # Leave group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        # get message that is sent
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to the group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to websocket
        await self.send(text_data=json.dumps({"message": message}))
