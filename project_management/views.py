from rest_framework import generics
from project_management.models import Project
from project_management.permissions import IsProjectManager
from rest_framework.permissions import IsAuthenticated
from project_management.serializers import ProjectSerializer
from rest_framework import status
from rest_framework.response import Response


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
