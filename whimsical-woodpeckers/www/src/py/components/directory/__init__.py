from pyvue import Component
from components.directory.user import User
from datetime import datetime
from fetch import Fetch
from websocket import WebSocket

# __pragma__ ('skip')
console = window = this = parent_this = JSON = 0
# __pragma__ ('noskip')


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
        this.id = 1234
        this.token = 1234
        parent_this.callbacks = 2
        parent_this = this

        def callback():
            parent_this.callbacks -= 1
            if parent_this.callbacks == 0:
                parent_this.socket = MessageSocket(lambda parent_this: parent_this.handle_message(this),
                                                   parent_this.token, parent_this.id)

        def data_callback(data):
            parent_this.id = data['id']
            callback()

        def auth_callback(data):
            parent_this.token = data['token']
            callback()

        Fetch.get("data/") \
            .then(lambda response: response.json()) \
            .then(lambda data: data_callback(data))
        Fetch.get("auth/") \
            .then(lambda response: response.json()) \
            .then(lambda data: auth_callback(data))

    @staticmethod
    def handle_message(data):
        pass


class MessageSocket(WebSocket):
    def __init__(self, component, token, id):
        room_name = "test"
        console.log(token, id)
        super().__init__('ws://'
                         + window.location.host
                         + '/ws/chat/'
                         + room_name
                         + '/')
        self.component = component
        self.send({"type": "auth", "auth_token": token, "id": id})

    def send_message(self, id, type, data):
        message = {"type": "message", "id": id, "data": {"text": data, "type": type}}
        self.send(message)

    def message(self, event):
        data = JSON.parse(event.data)
        self.callback(data)

    def send(self, data):
        super().send(JSON.stringify(data))
