
from pyvue import Component

class User(Component):
    data = ["name","last_online","id"]

    def list_name(self):
        return({ self.data.name })