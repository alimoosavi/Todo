from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from project_management.models import Developer, ProjectManager





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


DEVELOPER = 'Developer'
PROJECT_MANAGER = 'Project Manager'

VALID_ROLES = [DEVELOPER, PROJECT_MANAGER]


def validate_user_role(role: str):
    if role not in VALID_ROLES:
        raise ValidationError('invalid role')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    role = serializers.CharField(write_only=True, required=True, validators=[validate_user_role])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'password2',
                  'email',
                  'first_name',
                  'last_name',
                  'role')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        role = validated_data.get('role')
        if role == DEVELOPER:
            Developer.objects.create(user=user)
        elif role == PROJECT_MANAGER:
            ProjectManager.objects.create(user=user)

        return user
