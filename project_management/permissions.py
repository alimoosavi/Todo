from rest_framework.permissions import BasePermission

from todo_auth.models import UserProfile


class IsProjectManager(BasePermission):
    def has_permission(self, request, view):
        return UserProfile.objects.filter(user=request.user,
                                          role=UserProfile.PROJECT_MANAGER).exists()


class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        return UserProfile.objects.filter(user=request.user,
                                          role=UserProfile.DEVELOPER).exists()


class HasAccessToProject(BasePermission):
    def has_permission(self, request, view):
        project_pk = view.kwargs['project_pk'] \
            if request.method == 'GET' else request.data.get('project', None)
        if not project_pk:
            return False
        return UserProfile.objects.filter(user=request.user, projects__id__in=[project_pk])
