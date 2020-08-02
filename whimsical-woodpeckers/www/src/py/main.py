from pyvue import Vue


def next_message():
    # For right now, to access data in components you have to use this
    this.current += 1
    if this.current > len(this.messages) - 1:
        this.current = 0


def add_message():
    this.messages.append(this.textbox)
    this.textbox = ""


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
    methods = {
        "next": next_message,
        "add": add_message
    }


test2 = MessageList("#app1")

test3 = MessageList("#app2")

