from todo_auth.serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from todo_auth.models import UserProfile
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

from .permissions import IsProjectManager
from .serializers import RegisterSerializer
from rest_framework import generics
from todo_auth.serializers import DeveloperSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class DeveloperListViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsProjectManager,)
    serializer_class = DeveloperSerializer

    def get_queryset(self):
        developers_ids = UserProfile.objects \
            .filter(role=UserProfile.DEVELOPER) \
            .values('id')

        return User.objects.filter(id__in=developers_ids)
