import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from pyfiglet import figlet_format

welcome_text = (figlet_format('Wily Wolves', font='starwars') +
        f"\nThis is the Wily Wolves MUD project for the Python Discord: Summer-code-jam-2020"
        f"\nType 'login' if you already have an account or 'new' to start this journey!")

class MudConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'MUD'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'message': welcome_text
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        ### IMPORTANT ###
        # This message is what we'll use as command input
        # So here we'll split it and work with the commands

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))