import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from config.middleware import WebSocketJWTMiddleware
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from apps.pongue.routing import ws_urlpatterns as pongue_urlpatterns
from apps.notification.routing import ws_urlpatterns as notification_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            WebSocketJWTMiddleware(
                URLRouter(
                    [
                        *pongue_urlpatterns,
                        *notification_urlpatterns,
                    ]
                ),
            )
        ),
    }
)
