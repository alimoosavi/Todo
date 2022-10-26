from django.urls import path

from project_management.views import (ProjectCreateAndListViewSet,
                                      DeveloperListViewSet,
                                      AssignProjectToPMViewSet,
                                      AssignProjectToDeveloperViewSet,
                                      TaskListViewSet,
                                      TaskCreateViewSet,
                                      AssignTaskCreateViewSet,
                                      MyTaskListViewSet)

urlpatterns = [
    path('project/', ProjectCreateAndListViewSet.as_view(), name='project'),
    path('developers/', DeveloperListViewSet.as_view(), name='developers_list'),
    path('assign-project/pm/', AssignProjectToPMViewSet.as_view(), name='assign_project_pm'),
    path('assign-project/developer/', AssignProjectToDeveloperViewSet.as_view(), name='assign_project_dv'),
    path('task/', TaskCreateViewSet.as_view(), name='create_task'),
    path('task/<int:project_pk>/', TaskListViewSet.as_view(), name='list_tasks'),
    path('my-tasks/<int:project_pk>/', MyTaskListViewSet.as_view(), name='my_tasks'),
    path('assign-task/', AssignTaskCreateViewSet.as_view(), name='assign_task'),
]
