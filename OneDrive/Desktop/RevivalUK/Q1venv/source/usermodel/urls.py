
from django.urls import path
from .views import RegisterView, LogoutAPIView, SetNewPasswordAPIView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail, BlacklistTokenUpdateView#, index, room
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView,
)
# from channels.routing import ProtocolTypeRouter, URLRouter
# from .consumer import ChatConsumer
# from usermodel.consumer import ChatConsumer

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
#     path('', index, name='index'),
#     path('<str:room_name>/', room, name='room')
]


# application = ProtocolTypeRouter({
#     'websocket': URLRouter([
#         path('ws/usermodel/', ChatConsumer)

#     ])
# })
