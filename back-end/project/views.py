import asyncio

from ably import AblyRest
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from local_os import ABLY_API_KEY
from project.models import Project
from project.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdate(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Project.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        project = self.get_object()
        return Response({'project': project, 'room_name': project.pk}, template_name='project_update.html')

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class AblyProjectUpdate(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def retrieve(self, request, *args, **kwargs):
        project = self.get_object()
        return Response({'project': project, 'apiKey': ABLY_API_KEY}, template_name='ably_project_update.html')

    @action(methods=('post', 'get'), detail=False)
    def send_message(self, request, *args, **kwargs):
        message = request.POST.get('message')
        if message is not None:
            client = AblyRest(ABLY_API_KEY)
            channel = client.channels.get('sport')
            asyncio.run(channel.publish('update', message))
        return Response({'message': message}, template_name='publish.html')


def room(request, room_name):
    return render(request, 'project_detail.html', {
        'room_name': room_name
    })
