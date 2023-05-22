from django.urls import re_path

from project import consumers

websocket_urlpatterns = [
    re_path(r'project/colaboration/(?P<room_name>\w+)/$', consumers.ProjectRoomConsumer.as_asgi()),
]
