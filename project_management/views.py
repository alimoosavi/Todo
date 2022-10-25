from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from project_management.models import Project
from project_management.permissions import IsProjectManager, PMHasAccessToProject
from project_management.serializers import ProjectSerializer, AssignProjectToPMSerializer, \
    AssignProjectToDeveloperSerializer
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
    permission_classes = (IsAuthenticated, IsProjectManager, PMHasAccessToProject,)
