import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from .models import OnlineUsers
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

class MyAsyncWebSocketConsumner(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.group_name=self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await database_sync_to_async(OnlineUsers.objects.create)(name=self.scope['user'].username)
        await self.accept()  # Accept the WebSocket connection

    async def disconnect(self, close_code):
        # Perform WebSocket disconnection logic
        username = self.scope['user'].username
        await self.disconnect_user(username)

        raise StopConsumer()

    async def receive(self, text_data):
        # Handle incoming WebSocket messages
        data=json.loads(text_data)
        data['user']=self.scope['user'].username

        #Add chat into database query
        if self.scope['user'].is_authenticated:

            await self.channel_layer.group_send(self.group_name,{
                'type':'chat.message',
                'message':json.dumps(data)
            })
        else:
            await self.send(text_data=(json.dumps({
                'message':'Login Required'
            }))
            )


    async def chat_message(self,event):
        await self.send(text_data=json.dumps({
                'message':event['message']
            }))

    @database_sync_to_async
    def disconnect_user(self, name):
        # Retrieve the OnlineUsers object and delete it
        online_user = OnlineUsers.objects.filter(name=name).first()
        if online_user:
            online_user.delete()