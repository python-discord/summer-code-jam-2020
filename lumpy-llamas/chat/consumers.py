import json
import datetime
import logging
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db import transaction
from chat.models import ChatRoom, ChatMessage, User, _model_field_limits


logger = logging.getLogger(__name__)


class UserNotFound(Exception):
    pass


class ChatConsumer(AsyncWebsocketConsumer):
    @sync_to_async
    def create_or_get_group(self):
        chat_room, created = ChatRoom.objects.get_or_create(name=self.room_name)
        if created:
            logger.info(f'Created new chat_room "{self.room_name}"')
        return chat_room.pk

    @sync_to_async
    def get_user(self):
        user, created = User.objects.get_or_create(username=self.user.username)
        if created:
            logger.warning(f'New user "{self.user.username}" created during connection to room "{self.room_name}"')
        return user.pk

    async def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.room_id = self.create_or_get_group()
        self.user_id = self.get_user()

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        logger.info(f'User "{self.user.username}" is connected to room "{self.room_name}"')

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        logger.info(f'User "{self.user.username}" is disconnected to room "{self.room_name}"')

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Save message to database
        self.save_message(text_data_json)

        # Send message to room group
        message_to_send = {
            'type': 'chat_message',
            'message': {
                'message': text_data_json['message'],
                'datetime': text_data_json['datetime'],
                'user': self.user.username
            }
        }

        await self.channel_layer.group_send(
            self.room_group_name,
            message_to_send
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @sync_to_async
    def save_message(self, message_data):
        chunks, chunk_size = len(message_data['message']), _model_field_limits['Message__message__max_length']
        message_chunks = [message_data['message'][i:i + chunk_size] for i in range(0, chunks, chunk_size)]

        first_message_chunk = message_chunks.pop(0)

        with transaction.atomic():
            message = ChatMessage(
                chat_room_id=self.room_id,
                user_id=self.user_id,
                datetime=datetime.fromisoformat(message_data['datetime']),
                message=first_message_chunk
            )

            message.save()
            parent_message_id = message.pk

            for message_chunk in message_chunks:
                message = ChatMessage(
                    chat_room_id=self.room_id,
                    user_id=self.user_id,
                    datetime=datetime.fromisoformat(message_data['datetime']),
                    message=first_message_chunk,
                    parent_message_id=parent_message_id
                )
                message.save()
