from rest_framework.permissions import BasePermission
from todo_auth.models import UserProfile


class IsProjectManager(BasePermission):
    def has_permission(self, request, view):
        return UserProfile.objects.filter(user=request.user,
                                          role=UserProfile.PROJECT_MANAGER).exists()
