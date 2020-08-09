import json
from channels.generic.websocket import WebsocketConsumer
from anon.models import AnonUser
from asgiref.sync import async_to_sync
from messages.models import Conversation, UserChannels
from django.utils import timezone
import datetime

# __pragma__ ('skip')
convo = 0
# __pragma__ ('noskip')


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = None
        self.groups = set()

    def disconnect(self, close_code):
        UserChannels.objects.filter(name=self.channel_name).delete()

    def group_name(self, user):
        return f"messaging-{self.user.id}"

    def receive(self, text_data):
        try:
            data = json.loads(text_data)
            print(data)
        except json.JSONDecodeError:
            # self.disconnect(1)
            return
        command = data.get('type', None)
        print(data)
        if command == 'auth':
            user = AnonUser.objects.get(id=data.get("id"))
            if user:
                print(timezone.now() - datetime.timedelta(seconds=30), user.auth_expiration)
                if user.auth_expiration >= timezone.now() and user.auth_token == data.get('auth_token', None):
                    self.user = user
                    UserChannels.objects.create(name=self.channel_name, user=self.user)
                    print(self.group_name(user))
                    async_to_sync(self.channel_layer.group_add)(self.group_name(user), self.channel_name)
                    return
            self.disconnect(1)
        elif command == 'message' and self.user:
            other_user = AnonUser.objects.get(id=data.get("id"))
            if other_user.id < self.user.id:
                user_one = other_user
                user_two = self.user
            else:
                user_one = self.user
                user_two = other_user

            try:
                Conversation.objects.get(user_one=user_one, user_two=user_two)
            except Conversation.DoesNotExist:
                Conversation.objects.create(user_one=user_one, user_two=user_two)
            
            data['data']['from'] = self.user.id
            data['data']['to'] = other_user.id

            async_to_sync(self.channel_layer.group_send)(
                self.group_name(other_user),
                {
                    "type": "chat_message",
                    "data": data['data']
                }
            )

            async_to_sync(self.channel_layer.group_send)(
                self.group_name(self.user),
                {
                    "type": "chat_message",
                    "data": data['data']
                }
            )

    def chat_message(self, event):
        self.send(event['data'])
