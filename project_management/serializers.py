from rest_framework import serializers
from project_management.models import Project, Task
from todo_auth.models import UserProfile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description',)
        extra_kwargs = {
            'id': {'read_only': True},
            'creator': {'write_only': True}
        }


class AssignProjectToPMSerializer(serializers.ModelSerializer):
    project = serializers.IntegerField(write_only=True, required=True)

    def validate(self, attrs):
        if not Project.objects.filter(id=attrs['project']).exists():
            raise serializers.ValidationError({"project": "Project doesn't exist"})
        return attrs

    def create(self, validated_data):
        project_manager = UserProfile.objects.get(user=self.context['request'].user)
        project = Project.objects.get(id=validated_data['project'])
        project_manager.projects.add(project)
        return project_manager

    class Meta:
        model = UserProfile
        fields = ('project',)


class AssignProjectToDeveloperSerializer(serializers.ModelSerializer):
    project = serializers.IntegerField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        fields_error_dict = {}
        if not Project.objects.filter(id=attrs['project']).exists():
            fields_error_dict['project'] = "Project doesn't exist"
        if not UserProfile.objects.filter(user__username=attrs['username'],
                                          role=UserProfile.DEVELOPER).exists():
            fields_error_dict['username'] = "Developer with this username doesn't exist"

        if len(fields_error_dict) > 0:
            raise serializers.ValidationError(fields_error_dict)
        return attrs

    def create(self, validated_data):
        developer = UserProfile.objects.get(user__username=validated_data['username'])
        project = Project.objects.get(id=validated_data['project'])
        developer.projects.add(project)
        return developer

    class Meta:
        model = UserProfile
        fields = ('project', 'username',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'project',)


class AssignSerializer(serializers.Serializer):
    project = serializers.IntegerField(write_only=True, required=True)
    task = serializers.IntegerField(write_only=True, required=True)

    def validate(self, attrs):
        if not Task.objects.filter(id=attrs['task'], project_id=attrs['project']).exists():
            raise serializers.ValidationError({"task": "Task Id doesn't exist in project"})
        return attrs

    def create(self, validated_data):
        task = Task.objects.get(id=validated_data['task'])
        task.assignees.add(self.context['request'].user)
        return task

    class Meta:
        fields = ('project', 'task',)


class DeveloperSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False,
                                        read_only=True,
                                        slug_field='username')

    class Meta:
        model = UserProfile
        fields = ('user',)
