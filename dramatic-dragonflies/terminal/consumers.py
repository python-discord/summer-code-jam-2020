import json
import pprint

from channels.generic.websocket import WebsocketConsumer


# TODO: add auth (check self.scope for user)
class TerminalConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('got a connection')

    def disconnect(self, code):
        print('got a disconnection')

    def receive(self, text_data=None, bytes_data=None):
        pprint.pp(json.loads(text_data))
