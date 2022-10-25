from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True, blank=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(User)
