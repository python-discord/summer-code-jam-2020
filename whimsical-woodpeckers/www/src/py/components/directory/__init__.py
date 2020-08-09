from pyvue import Component
from components.directory.user import User
from datetime import datetime
from fetch import Fetch
from websocket import WebSocket

users = [
    {"name": "John Doe", "last_online": datetime.now().strftime("%B %d, %Y , %H:%M"), "id": 1}

]


class Directory(Component):
    data = {
        'users': users,
    }
    components = {
        "user": User.get_component()
    }

    template = "#directory-template"

    props = ['mode']

    @staticmethod
    def created():
        print("help")
        this.create_socket()

    @staticmethod
    def create_socket():
        # Get info about our authentication
        callbacks = 2
        id = None
        token = None
        parent_this = this

        def callback():
            callbacks -= 1
            if callbacks == 0:
                parent_this.socket = MessageSocket(lambda parent_this: parent_this.handle_message(this), token, id)

        def data_callback(data):
            id = data['id']
            callback()

        def auth_callback(data):
            token = data['token']
            callback()

        Fetch.get("./data") \
            .then(lambda response: response.json()) \
            .then(lambda data: data_callback(data))
        Fetch.get("./auth") \
            .then(lambda response: response.json()) \
            .then(lambda data: auth_callback(data))

    @staticmethod
    def handle_message(data):
        pass



class MessageSocket(WebSocket):
    def __init__(self, component, token, id):
        room_name = "test"
        super().__init__('ws://'
                         + "127.0.0.1"
                         + '/ws/chat/'
                         + room_name
                         + '/')
        self.component = component
        self.send({"type": "auth",  "auth_token": token, "id": id})

    def send_message(self, id, type, data):
        message = {"type": "message", "id": id, "data": {"text": data, "type": type}}
        self.send(message)

    def message(self, event):
        data = JSON.parse(event.data)
        self.callback(data)

    def send(self, data):
        super().send(JSON.stringify(data))
