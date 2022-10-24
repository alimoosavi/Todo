from django.urls import path

from project_management.views import ProjectCreateAndListViewSet

urlpatterns = [
    path('project/', ProjectCreateAndListViewSet.as_view(), name='project_api'),
]
