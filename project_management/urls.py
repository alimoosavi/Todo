from django.urls import path

from project_management.views import ProjectCreateAndListViewSet, DeveloperListViewSet, AssignProjectToPMViewSet, \
    AssignProjectToDeveloperViewSet

urlpatterns = [
    path('project/', ProjectCreateAndListViewSet.as_view(), name='project'),
    path('developers/', DeveloperListViewSet.as_view(), name='developers_list'),
    path('assign-project/pm/', AssignProjectToPMViewSet.as_view(), name='assign_project_pm'),
    path('assign-project/developer/', AssignProjectToDeveloperViewSet.as_view(), name='assign_project_dv')
]
