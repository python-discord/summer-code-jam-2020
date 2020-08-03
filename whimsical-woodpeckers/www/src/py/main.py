from pyvue import Vue


class MessageList(Vue):
    data = {
        "current": 0,
        "textbox": "",
        "messages": [
            "Hi there!",
            "Welcome to PyVue!",
            "Hope it goes well for you!"
        ]
    }

    def next_message(self):
        self.data['current'] += 1
        if self.data['current'] > len(self.data['messages']) - 1:
            self.data['current'] = 0

    def add_message(self):
        self.data['messages'].append(self.data['textbox'])
        self.data['textbox'] = ""


class Login(Vue):
    data = {
        "username": "",
        "password": "",
        "testArea": "",
    }

    def login(self):
        self.data['testArea'] = self.data['username']
        self.data['testArea'] += ":"
        self.data['testArea'] += self.data['password']


test_login = Login("#login")

test2 = MessageList("#app1")

test3 = MessageList("#app2")
