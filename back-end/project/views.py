from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from project.models import Project
from project.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Project.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        project = self.get_object()
        return Response({'project': project, 'room_name': project.pk}, template_name='project_detail.html')

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


def room(request, room_name):
    return render(request, 'project_detail.html', {
        'room_name': room_name
    })
