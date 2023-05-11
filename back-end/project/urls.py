from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project import views

router = DefaultRouter()
router.register('project', views.ProjectViewSet, basename="project")

urlpatterns = [
    path('', include(router.urls)),
]
