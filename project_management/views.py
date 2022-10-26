from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from project_management.models import Project, Task
from project_management.permissions import (IsProjectManager,
                                            HasAccessToProject,
                                            IsDeveloper)
from project_management.serializers import (ProjectSerializer,
                                            AssignProjectToPMSerializer,
                                            AssignProjectToDeveloperSerializer,
                                            TaskSerializer,
                                            AssignSerializer)
from todo_auth.models import UserProfile
from todo_auth.serializers import DeveloperSerializer


class DeveloperListViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsProjectManager,)
    queryset = UserProfile.objects.filter(role=UserProfile.DEVELOPER)
    serializer_class = DeveloperSerializer


class ProjectCreateAndListViewSet(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsProjectManager,)
    queryset = Project.objects.all()


class AssignProjectToPMViewSet(generics.CreateAPIView):
    serializer_class = AssignProjectToPMSerializer
    permission_classes = (IsAuthenticated, IsProjectManager,)


class AssignProjectToDeveloperViewSet(generics.CreateAPIView):
    serializer_class = AssignProjectToDeveloperSerializer
    permission_classes = (IsAuthenticated, IsProjectManager, HasAccessToProject,)


class TaskListViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated, HasAccessToProject,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_pk = self.kwargs['project_pk']
        return Task.objects.filter(project_id=project_pk)


class TaskCreateViewSet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, HasAccessToProject,)
    serializer_class = TaskSerializer


class AssignTaskCreateViewSet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsDeveloper, HasAccessToProject,)
    serializer_class = AssignSerializer
