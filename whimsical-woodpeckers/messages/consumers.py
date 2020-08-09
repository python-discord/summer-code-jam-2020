import json
from channels.generic.websocket import WebsocketConsumer
from anon.models import AnonUser


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('hell yah')
        self.accept()
        self.user = None

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except json.JSONDecodeError:
            self.disconnect()
        command = data.get('type', None)
        if command == 'auth':
            AnonUser.objects.get(id=)
        elif command == 'message':

            message = data['message']

            # self.send(text_data=json.dumps({
            #     'message': message
            # }))
