from datetime import datetime

from pyvue import Vue, Component


class App(Vue):
    data = {
        "username": "",
        "password": "",
        "testArea": "",
        "friendListName": "Friends",
        "chatName": "John Doe",
        "current_user": "Jane Doe",
    }

    def login(self):
        # send login info
        pass


messages = [
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
]


class Messages(Component):

    data = {
        'messages': messages,
        'current_user': 'Jane Doe',
    }

    template = '<div><div v-for="message in messages" :key="message.content" v-bind:class="{ \'alert-primary\': (current_user==message.sender), \'alert-info\':(current_user!=message.sender) }" class="alert">' \
        '<span data-toggle="tooltip" data-placement="top" v-bind:title="message.time">{{ message.sender }}</span>' \
        ': {{ message.content }}</div></div>'

    # template = "#messages"


message_component = Messages()
app = App('#app')
