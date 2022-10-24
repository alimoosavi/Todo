from rest_framework import serializers
from project_management.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'creator')
        extra_kwargs = {
            'id': {'read_only': True},
            'creator': {'write_only': True}
        }
