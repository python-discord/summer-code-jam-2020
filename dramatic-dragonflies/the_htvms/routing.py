from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# http -> django is automatically added
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            []
        )
    )
})
