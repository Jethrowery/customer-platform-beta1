# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from usermodel.consumer import ChatConsumer

# application = ProtocolTypeRouter({
#     'websocket': URLRouter([
#         path('ws/usermodel/', ChatConsumer)
        
#     ]) 
# })

# from django.urls import re_path

# from . import consumer

# websocket_urlpatterns = [
#     re_path(r'ws/usermodel/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
# ]
