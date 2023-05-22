import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ProjectRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        user_email = text_data_json['user_email']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'project_update',
                'action': action,
                'user_email': user_email,
            }
        )

    async def project_update(self, event):
        action = event['action']
        user_email = event['user_email']

        await self.send(text_data=json.dumps({
            'action': action,
            'user_email': user_email,
        }))
