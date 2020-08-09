from django.urls import re_path
from . import consumers
websocket_patterns = [
    re_path(r"^ws/terminal/(?P<storage_id>\d+)/(?P<vm_id>\d+)$", consumers.TerminalConsumer)
]
