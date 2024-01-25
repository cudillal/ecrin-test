from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title