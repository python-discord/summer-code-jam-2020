from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
import shinny_sheep.chat.routing as chat.routing

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
