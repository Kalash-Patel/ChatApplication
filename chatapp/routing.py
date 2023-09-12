from django.urls import path
from chatapp import consumers

websocket_urlpatterns=[
    path('api/chat/send/<str:group_name>/', consumers.MyAsyncWebSocketConsumner.as_asgi()),
]