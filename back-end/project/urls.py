from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from project import views
from project.views import ProjectDetail

router = DefaultRouter()
router.register('projects', views.ProjectViewSet, basename="project")

urlpatterns = [
    path('', include(router.urls)),
    path(r'project_detail/<int:pk>/', ProjectDetail.as_view()),
]
