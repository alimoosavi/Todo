from django.db import models
from django.contrib.auth.models import User


class OperativeModel(models.Model):
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Project(OperativeModel):
    title = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)


class Task(OperativeModel):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True, blank=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.OneToOneField(Project,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True)


class ProjectManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, null=True, blank=True)
