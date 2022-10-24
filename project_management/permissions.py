from rest_framework.permissions import BasePermission
from project_management.models import ProjectManager


class IsProjectManager(BasePermission):
    def has_permission(self, request, view):
        return ProjectManager.objects.filter(user=request.user).exists()
