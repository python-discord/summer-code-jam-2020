from pyvue import Vue, Component
from components.directory import Directory
from components.messages import Message, Messages


class App(Vue):
    template = "#app-template"
    data = {
        "mode": 0  # UI mode
    }
    components = {
        "directory": Directory.get_component(),
        "messages": Messages.get_component(),
        "message": Message.get_component()
    }




