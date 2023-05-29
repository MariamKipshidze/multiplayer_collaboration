from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project import views
from project.views import ProjectUpdate

router = DefaultRouter()
router.register('projects', views.ProjectViewSet, basename="project")
router.register('ably_project_update', views.AblyProjectUpdate, basename='ably_project_update')

urlpatterns = [
    path('', include(router.urls)),
    path(r'project_update/<int:pk>/', ProjectUpdate.as_view()),
    path(r'detail_room/<str:room_name>/', views.room, name='room'),
]
