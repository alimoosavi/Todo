from django.urls import path

from project_management.views import ProjectCreateAndListViewSet, DeveloperListViewSet

urlpatterns = [
    path('project/', ProjectCreateAndListViewSet.as_view(), name='project_api'),
    path('developers/', DeveloperListViewSet.as_view(), name='developers_list_api')
]
