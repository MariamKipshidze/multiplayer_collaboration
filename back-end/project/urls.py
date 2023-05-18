from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project import views
from project.views import ProjectDetail

router = DefaultRouter()
router.register('projects', views.ProjectViewSet, basename="project")

urlpatterns = [
    path('', include(router.urls)),
    # path(r'project_detail/<int:pk>/', ProjectDetail.as_view()),
    # path('<str:room_name>/<int:pk>/', ProjectDetail.as_view(), name='room'),
    path('<str:room_name>/', views.room, name='room'),
]
