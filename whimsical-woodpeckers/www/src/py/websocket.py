# __pragma__ ('skip')
window = JSON = this = js_websocket = __new__ = 0    # Prevent complaints by optional static checker
# __pragma__ ('noskip')


# __pragma__("kwargs")
class WebSocket:
    def __init__(self, url, protocols=None):
        self._socket = __new__(window.WebSocket(url, protocols))
        self._socket.onmessage = lambda event: self.on_message(event)
        self._socket.onerror = lambda: self.on_error()
        self._socket.onclose = lambda event: self.on_close(event)
        self._socket.onopen = lambda event: self.on_open(event)

    def send(self, data):
        self._socket.send(data)

    def close(self, code=None, reason=None):
        self._socket.close()

    def on_message(self, event):
        pass

    def on_error(self):
        pass

    def on_open(self, event):
        pass

    def on_close(self, event):
        pass

# __pragma__("nokwargs")
