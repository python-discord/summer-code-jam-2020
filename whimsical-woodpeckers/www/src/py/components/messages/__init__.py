from datetime import datetime
from pyvue import Component


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
    }
    components = {
        "message": Message.get_component()
    }

    template = "#messages-template"
