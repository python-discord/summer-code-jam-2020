from django.urls import re_path, include
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
import battle.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path('^ws/battle/', include(battle.routing)),
            re_path('^ws/chat/', include(chat.routing)),
        ])
    ),
})
