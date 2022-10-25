from rest_framework.permissions import BasePermission

from project_management.models import Project
from todo_auth.models import UserProfile


class IsProjectManager(BasePermission):
    def has_permission(self, request, view):
        return UserProfile.objects.filter(user=request.user,
                                          role=UserProfile.PROJECT_MANAGER).exists()


class PMHasAccessToProject(BasePermission):
    def has_permission(self, request, view):
        project = request.data.get('project', None)
        if not project:
            return False

        return UserProfile.objects.filter(user=request.user,
                                          role=UserProfile.PROJECT_MANAGER,
                                          projects__id__in=[project])
