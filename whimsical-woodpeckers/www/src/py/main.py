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
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
]


class MessageComponent(Component):

    data = {
        'messages': messages,
        'current_user': 'Jane Doe',
    }

    template = '<div><div v-for="message in messages" :key="message.content" v-bind:class="{ \'alert-primary\': (current_user==message.sender), \'alert-info\':(current_user!=message.sender) }" class="alert">' \
        '<span data-toggle="tooltip" data-placement="top" v-bind:title="message.time">{{ message.sender }}</span>' \
        ': {{ message.content }}</div></div>'


message_component = MessageComponent()
app = App('#app')

# class MessageList(Vue):
#     data = {
#         "current": 0,
#         "textbox": "",
#         "messages": [
#             "Hi there!",
#             "Welcome to PyVue!",
#             "Hope it goes well for you!"
#         ]
#     }
#
#     def next_message(self):
#         self.data['current'] += 1
#         if self.data['current'] > len(self.data['messages']) - 1:
#             self.data['current'] = 0
#
#     def add_message(self):
#         self.data['messages'].append(self.data['textbox'])
#         self.data['textbox'] = ""


# test2 = MessageList("#app1")
# test3 = MessageList("#app2")
