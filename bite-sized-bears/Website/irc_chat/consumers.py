import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from django.db.models import F
from channels.db import database_sync_to_async

from .models import Message, UserProfile
from syndication_app.models import User


class ChatConsumer(WebsocketConsumer):

    @database_sync_to_async
    def update_user_incr(self, community_name):
        present = UserProfile.objects.filter(community__exact=community_name)
        print(present)
        if len(present) == 0:
            UserProfile.objects.create(community=community_name,
                                       count=0)
        what = UserProfile.objects.filter(community__exact=community_name)\
            .update(count=F('count') + 1)
        print(what)

    @database_sync_to_async
    def update_user_decr(self, community_name):
        print(community_name)
        what = UserProfile.objects.filter(community__exact=community_name)\
            .update(count=F('count') - 1)
        print(what)

    def fetch_messages(self, data):  # noqa
        messages = Message.last_15_messages(self=Message, community=self.room_name)  # noqa
        print(messages)
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author = data['from']
        author_user = User.objects.get(name=author)
        message = Message.objects.create(
            author=author_user,
            content=data['message'],
            community=self.room_name)
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):  # noqa
        return {
            'author': message.author.name,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']  # noqa
        self.update_user_incr(self.room_name)
        self.room_group_name = 'chat_%s' % self.room_name  # noqa
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        print("Accepted")
        print(self.room_name + ": count :",
              UserProfile.objects.filter(community__exact=self.room_name).values('count'))

    def disconnect(self, close_code):  # noqa
        print("DISCONNECTING")
        self.update_user_decr(self.room_name)
        print("Done ... decremented")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print(self.room_name + ": count :",
              UserProfile.objects.filter(community__exact=self.room_name).values('count'))

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        print(self.room_name + ": count :",
              UserProfile.objects.filter(community__exact=self.room_name).values('count'))
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        print(self.room_name + ": count :",
              UserProfile.objects.filter(community__exact=self.room_name).values('count'))
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        print(self.room_name + ": count :",
              UserProfile.objects.filter(community__exact=self.room_name).values('count'))
        message = event['message']
        self.send(text_data=json.dumps(message))
