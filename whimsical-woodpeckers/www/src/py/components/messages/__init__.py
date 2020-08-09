from datetime import datetime
from pyvue import Component
#from websocket import WebSocket
from common import MessageTypes

# __pragma__ ('skip')
console = window = 0
# __pragma__ ('noskip')

console.log(MessageTypes)

# __pragma__ ('skip')
window = JSON = this = 0    # Prevent complaints by optional static checker
# __pragma__ ('noskip')

messages = [
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time":
        datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
]


class Message(Component):
    data = {
        'currentUser': 'Jane Doe',

    }
    props = ['title', 'sender', 'content', 'time']
    template = "#message-template"


class Messages(Component):
    data = {
        'messages': messages,
        'chatName': 'John Doe',
    }
    components = {
        "message": Message.get_component()
    }

    props = ['mode']
    template = "#messages-template"

    # @staticmethod
    # def created():
    #     def new_message(data):
    #         if data['type'] == "message":
    #             this.messages.append(data['data'])
    #
    #     this.socket = MessageSocket(new_message)
