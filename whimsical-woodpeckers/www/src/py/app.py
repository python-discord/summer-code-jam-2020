from pyvue import Vue
# from components.directory import Directory
# from components.messages import Messages
from components.display import Desktop, Mobile

# __pragma__ ('skip')
navigator = window = 0
# __pragma__ ('noskip')


class App(Vue):
    template = "#app-template"
    data = {
        "mode": 1  # UI mode
    }
    components = {
        "desktop": Desktop.get_component(),
        "mobile": Mobile.get_component()
    }
