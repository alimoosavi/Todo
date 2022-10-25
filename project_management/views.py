from rest_framework import generics
from todo_auth.models import UserProfile
from project_management.models import Project
from project_management.permissions import IsProjectManager, PMHasAccessToProject
from rest_framework.permissions import IsAuthenticated
from project_management.serializers import ProjectSerializer, AssignProjectToPMSerializer, \
    AssignProjectToDeveloperSerializer
from todo_auth.serializers import DeveloperSerializer
from rest_framework import status
from rest_framework.response import Response


class DeveloperListViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsProjectManager,)
    queryset = UserProfile.objects.filter(role=UserProfile.DEVELOPER)
    serializer_class = DeveloperSerializer


class ProjectCreateAndListViewSet(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsProjectManager,)
    queryset = Project.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={**request.data,
                                               'creator': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AssignProjectToPMViewSet(generics.CreateAPIView):
    serializer_class = AssignProjectToPMSerializer
    permission_classes = (IsAuthenticated, IsProjectManager,)


class AssignProjectToDeveloperViewSet(generics.CreateAPIView):
    serializer_class = AssignProjectToDeveloperSerializer
    permission_classes = (IsAuthenticated, IsProjectManager, PMHasAccessToProject,)
