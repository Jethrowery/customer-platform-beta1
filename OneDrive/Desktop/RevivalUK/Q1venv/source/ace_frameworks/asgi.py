"""
ASGI config for ace_frameworks project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# # import os

# # from django.core.asgi import get_asgi_application
# # from channels.routing import ProtocolTypeRouter
# from channels.routing import get_default_application


# import usermodel.routing
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ace_frameworks.settings')

#application = get_asgi_application()
# # application = ProtocolTypeRouter({
# #     "http": get_asgi_application(),
# #     # Just HTTP for now. (We can add other protocols later.)
# # })


# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#       URLRouter(
#             usermodel.routing.websocket_urlpatterns
#         )
#       ),
# })
