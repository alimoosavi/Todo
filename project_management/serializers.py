from rest_framework import serializers
from project_management.models import Project, Developer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'creator')
        extra_kwargs = {
            'id': {'read_only': True},
            'creator': {'write_only': True}
        }


class DeveloperSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False,
                                        read_only=True,
                                        slug_field='username')

    class Meta:
        model = Developer
        fields = ('user',)
