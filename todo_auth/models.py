from django.db import models
from django.contrib.auth.models import User
from project_management.models import Project


class UserProfile(models.Model):
    DEVELOPER = 'Developer'
    PROJECT_MANAGER = 'Project Manager'

    ROLE_CHOICES = (
        ('Developer', DEVELOPER),
        ('Project Manager', PROJECT_MANAGER),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, null=True, blank=True)
