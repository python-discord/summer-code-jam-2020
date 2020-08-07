from pyvue import Component
from components.directory.user import User
from datetime import datetime

users = [
    {"name":"John Doe", "last_online":datetime.now().strftime("%B %d, %Y , %H:%M"), "id":1}

]

class Directory(Component):
    data = {
        'users': users,
    }
    components = {
        "user": User.get_component()
    }

    template = "#directory-template"
