from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Developer', 'Developer'),
        ('Project Manager', 'Project Manager'),
    )
    
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s's profile" % self.user
