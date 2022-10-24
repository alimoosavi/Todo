from django.urls import path
from todo_auth.views import MyObtainTokenPairView, RegisterView, DeveloperListViewSet
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('developers/', DeveloperListViewSet.as_view(), name='developers_list_api')
]
