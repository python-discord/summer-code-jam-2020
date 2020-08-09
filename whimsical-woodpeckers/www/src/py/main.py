from pyvue import Vue, Component
from app import App
# from fetch import Fetch

# __pragma__ ('skip')
this = console = 0    # Prevent complaints by optional static checker
# __pragma__ ('noskip')


# Components are a little hacky and not very pythonic but they are functional now
class Example(Component):
    template = "<div><div v-on:click='change'>{{ text }}</div><colorthing testprop='sample prop text'/></div>"
    data = {
        "text": "Example text"
    }

    @staticmethod   # All methods must be declared as static
    def change():
        this.text = "new text"  # yep you access it through this. not pythonic, couldn't find a better way right now


Example()   # This registers it globally. You can see it referenced in the HTML


class ColorThing(Component):    # components are always referenced in all lowercase
    template = "#color-thing-template"  # Template is in the HTML, probably the way to do it for most things
    props = ['testprop']
    data = {
        "index": 0,
        "colors": [
            "yellow",
            "red",
            "blue"
        ]
    }

    @staticmethod
    def change():
        console.log(this)
        this.index += 1
        if this.index >= len(this.colors):
            this.index = 0


ColorThing()


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

# test3 = MessageList("#app2")

app = App("#app")
