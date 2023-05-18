from django.urls import re_path

from project import consumers

websocket_urlpatterns = [
    re_path(r'project/colaboration/(?P<project_room>\w+)/$', consumers.ProjectRoomConcumer),
]
