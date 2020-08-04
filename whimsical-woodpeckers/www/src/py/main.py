from pyvue import Vue

logo = {}

logo['messenger'] = 'https://media.discordapp.net/attachments/' \
    '737282857327788042/739220722194317322/Asset_26x.png?width=571&height=677'

logo['aol'] = 'https://media.discordapp.net/attachments/' \
    '737282857327788042/739220747582439494/Asset_16x.png?width=918&height=677'

logo['irc'] = 'https://www.plutora.com/wp-content/uploads/2018/11/irc_internet_relay_chat.png'

logo['woodpeckers'] = 'https://media.discordapp.net/attachments/' \
    '737282857327788042/739220734328569916/Asset_36x.png?width=1441&height=590'

logo['current'] = logo['messenger']


class App(Vue):
    data = {
        "username": "",
        "password": "",
        "testArea": "",
        "friendListName": "Friends",
        "chatName": "John Doe",
    }

    def login(self):
        # send login info
        pass


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

# test2 = MessageList("#app1")
#
# test3 = MessageList("#app2")


app = App("#app")
